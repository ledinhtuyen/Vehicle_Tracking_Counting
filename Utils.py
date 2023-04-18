import cv2
import random
import numpy as np
from collections import deque
import yolov5
import torch
import time
from PySide2.QtCore import QThread, Signal
from trackers.multi_tracker import create_tracker

limits = [80, 250, 550, 250]
model = yolov5.load('yolov5n.onnx', device='cpu')
model.classes = [2, 3, 5, 7]
tracker = create_tracker('botsort')
class VideoStream(QThread):
    signal = Signal(np.ndarray)

    def __init__(self, index):
        super(VideoStream, self).__init__()
        self.index = index
        print("start threading", self.index)
        self.video_path = None
        self.isTracking = False
        self.isCount = False
        self.data_deque = {}
        self.mask = None
        self.count = 0
        self.totalCount = []
        self.cap = None

    def run(self):
        scaler = 1
        while True:
            start_time = time.time()
            ret, frame = self.cap.read()
            if ret:
                frameRegion = cv2.bitwise_and(frame, self.mask)
                results = model(frameRegion)
                if self.isTracking or self.isCount:
                    resultsTracker = tracker.update(results.pred[0].cpu(), frame)
                
                if self.isTracking:
                    if resultsTracker.shape[0] > 0:
                        frame = self.draw_boxes(frame, resultsTracker[:, 0:4], model.names, resultsTracker[:, 5], resultsTracker[:, 4])
                else:

                    frame = self.draw_boxes(frame, results.xyxy[0][:, 0:4], model.names, results.xyxy[0][:, 5])
                
                if self.isCount:
                    frame = cv2.rectangle(frame, (limits[0], limits[1]), (limits[2], limits[3]), (0, 255, 0), 3 * scaler)

                    self.count = self.counting(frame, resultsTracker)
                    frame = cv2.putText(frame, 'Vehicle Count : ' + str(self.count), (25 * scaler, 100 * scaler), cv2.FONT_HERSHEY_SIMPLEX,
                                        1 * scaler, (255, 0, 255), 1 * scaler)

                end_time = time.time()
                FPS = 1 / (end_time - start_time)
                frame = cv2.putText(frame, 'FPS : ' + str(int(FPS)), (25 * scaler, 50 * scaler),
                        cv2.FONT_HERSHEY_SIMPLEX, 1 * scaler, (255, 0, 255), 1 * scaler)
                
                self.signal.emit(frame)
            else:
                self.cap.release()
                exit()
        self.cap.release()

    def draw_border(self, img, pt1, pt2, color, thickness, r, d):
        x1,y1 = pt1
        x2,y2 = pt2
        # Top left
        cv2.line(img, (x1 + r, y1), (x1 + r + d, y1), color, thickness)
        cv2.line(img, (x1, y1 + r), (x1, y1 + r + d), color, thickness)
        cv2.ellipse(img, (x1 + r, y1 + r), (r, r), 180, 0, 90, color, thickness)
        # Top right
        cv2.line(img, (x2 - r, y1), (x2 - r - d, y1), color, thickness)
        cv2.line(img, (x2, y1 + r), (x2, y1 + r + d), color, thickness)
        cv2.ellipse(img, (x2 - r, y1 + r), (r, r), 270, 0, 90, color, thickness)
        # Bottom left
        cv2.line(img, (x1 + r, y2), (x1 + r + d, y2), color, thickness)
        cv2.line(img, (x1, y2 - r), (x1, y2 - r - d), color, thickness)
        cv2.ellipse(img, (x1 + r, y2 - r), (r, r), 90, 0, 90, color, thickness)
        # Bottom right
        cv2.line(img, (x2 - r, y2), (x2 - r - d, y2), color, thickness)
        cv2.line(img, (x2, y2 - r), (x2, y2 - r - d), color, thickness)
        cv2.ellipse(img, (x2 - r, y2 - r), (r, r), 0, 0, 90, color, thickness)

        cv2.rectangle(img, (x1 + r, y1), (x2 - r, y2), color, -1, cv2.LINE_AA)
        cv2.rectangle(img, (x1, y1 + r), (x2, y2 - r - d), color, -1, cv2.LINE_AA)
        
        cv2.circle(img, (x1 +r, y1+r), 2, color, 12)
        cv2.circle(img, (x2 -r, y1+r), 2, color, 12)
        cv2.circle(img, (x1 +r, y2-r), 2, color, 12)
        cv2.circle(img, (x2 -r, y2-r), 2, color, 12)
    
        return img

    def compute_color_for_labels(self, label):
        """
        Simple function that adds fixed color depending on the class
        """
        if label == 7: # Truck
            color = (85,45,255)
        elif label == 2: # Car
            color = (222,82,175)
        elif label == 3:  # Motobike
            color = (0, 204, 255)
        elif label == 5:  # Bus
            color = (0, 149, 255)
        return color

    def UI_box(self, x, img, color=None, label=None, line_thickness=None):
        # Plots one bounding box on image img
        tl = line_thickness or round(0.002 * (img.shape[0] + img.shape[1]) / 2) + 1  # line/font thickness
        color = color or [random.randint(0, 255) for _ in range(3)]
        c1, c2 = (int(x[0]), int(x[1])), (int(x[2]), int(x[3]))
        cv2.rectangle(img, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
        if label:
            tf = max(tl - 1, 1)  # font thickness
            t_size = cv2.getTextSize(label, 0, fontScale=tl/3, thickness=tf)[0]

            img = self.draw_border(img, (c1[0], c1[1] - t_size[1] -3), (c1[0] + t_size[0], c1[1]+3), color, 1, 8, 2)

            cv2.putText(img, label, (c1[0], c1[1] - 2), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)

    def draw_boxes(self, img, bbox, names, object_id, identities=None, offset=(0, 0)):
        height, width, _ = img.shape
        # remove tracked point from buffer if object is lost
        if identities is not None:
            for key in list(self.data_deque):
                if key not in identities:
                    self.data_deque.pop(key)

        for i, box in enumerate(bbox):
            x1, y1, x2, y2 = [int(i) for i in box]
            x1 += offset[0]
            x2 += offset[0]
            y1 += offset[1]
            y2 += offset[1]

            # code to find center of bottom edge
            center = (int((x2+x1)/ 2), int((y2+y2)/2))

            # get ID of object
            id = int(identities[i]) if identities is not None else 0

            # create new buffer for new object
            if id not in self.data_deque and id != 0:  
                self.data_deque[id] = deque(maxlen= 64)
            color = self.compute_color_for_labels(object_id[i])
            obj_name = names[int(object_id[i])]
            label = '{}{:d}'.format("", id) + ":"+ '%s' % (obj_name) if id != 0 else '%s' % (obj_name)

            # add center to buffer
            if id != 0:
                self.data_deque[id].appendleft(center)
                # draw trail
                for i in range(1, len(self.data_deque[id])):
                    # check if on buffer value is none
                    if self.data_deque[id][i - 1] is None or self.data_deque[id][i] is None:
                        continue
                    # generate dynamic thickness of trails
                    thickness = int(np.sqrt(64 / float(i + i)) * 1.5)
                    # draw trails
                    cv2.line(img, self.data_deque[id][i - 1], self.data_deque[id][i], color, thickness)
            self.UI_box(box, img, label=label, color=color, line_thickness=2)
        return img

    def counting(self, frame, results):
        for i, res in enumerate(results):
            x1, y1, x2, y2, id = res[0], res[1], res[2], res[3], res[4]
            center = (int((x2+x1)/ 2), int((y2+y1)/2))
            if limits[0] < center[0] < limits[2] and limits[1] - 40 < center[1] < limits[3] + 40:
                if self.totalCount.count(id) == 0:
                    self.totalCount.append(id)
                    self.count += 1
        return self.count