import cv2
import time
import yolov5
import Utils
import torch
from trackers.multi_tracker import create_tracker

tracker = create_tracker('ocsort')

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

model = yolov5.load('yolov5s.pt', device=device)

model.classes = [2, 3, 5, 7]

video_path = 'video_test/test4.mp4'

cap = cv2.VideoCapture(video_path)
cv2.namedWindow('Video')

while True:
    if not cap.isOpened():
      print("Không thể mở file")
      exit()

    ret, frame = cap.read()
    start_time = time.time()

    if not ret:
        break

    if ret == True:
      results = model(frame)
      results = tracker.update(results.pred[0].cpu(), frame)
      # break
      if results.shape[0] > 0:
        frame = Utils.draw_boxes(frame, results[:, 0:4], model.names, results[:, 5], results[:, 4])

      end_time = time.time()
      FPS = 1 / (end_time - start_time)
      scaler = 1
      frame = cv2.putText(frame, 'FPS : ' + str(int(FPS)), (25 * scaler, 50 * scaler),
                      cv2.FONT_HERSHEY_SIMPLEX, 1.25 * scaler, (255, 0, 255), 2 * scaler)
      cv2.imshow('Video', frame)

    if cv2.waitKey(1) == ord('q'):
      break

cv2.destroyAllWindows()
cap.release()