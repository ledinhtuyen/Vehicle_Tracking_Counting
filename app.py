import sys
import cv2
from PySide2.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtCore import Qt

from GUI.Ui_App import Ui_App
from Utils import *

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_app = Ui_App()
        self.ui_app.setupUi(self)
        self.video_stream = {}

        self.ui_app.startVideo1.clicked.connect(lambda: self.streamVideo(1))
        self.ui_app.startVideo2.clicked.connect(lambda: self.streamVideo(2))
        self.ui_app.checkBoxTrack1.stateChanged.connect(lambda: self.turn_tracking(1))
        self.ui_app.checkBoxTrack2.stateChanged.connect(lambda: self.turn_tracking(2))
        self.ui_app.checkBoxCount1.stateChanged.connect(lambda: self.turn_count(1))
        self.ui_app.checkBoxCount2.stateChanged.connect(lambda: self.turn_count(2))
        self.ui_app.labelVideo1.mousePressEvent = lambda event: self.loadVideoFile(1, event)
        self.ui_app.labelVideo2.mousePressEvent = lambda event: self.loadVideoFile(2, event)

    def streamVideo(self, id):
        try:
            self.video_stream[id].start()
        except:
            QMessageBox.warning(self, "Warning", "Please load video file first")
    def render(self, id, cv_img):
        qt_img = self.convert_cv_qt(id, cv_img)
        self.ui_app.__getattribute__(f"labelVideo{id}").setPixmap(qt_img)
    def convert_cv_qt(self, id, cv_img):
        cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        height, width, channel = cv_img.shape
        bytesPerLine = channel * width
        convertToQtFormat = QImage(cv_img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        return QPixmap.fromImage(convertToQtFormat)
    def turn_tracking(self, id):
        try:
            self.video_stream[id].isTracking = self.ui_app.__getattribute__(f"checkBoxTrack{id}").isChecked()
        except:
            QMessageBox.warning(self, "Warning", "Please load video file first")
    def turn_count(self, id):
        try:
            self.video_stream[id].isCount = self.ui_app.__getattribute__(f"checkBoxCount{id}").isChecked()
        except:
            QMessageBox.warning(self, "Warning", "Please load video file first")
    def loadVideoFile(self, id, event):
        if event.button() == Qt.LeftButton:
            file_path, _ = QFileDialog.getOpenFileName(self, "Select video file", "", "Video files (*.mp4 *.avi *.mov)")
            if file_path:
                self.video_stream[id] = VideoStream(id)
                self.video_stream[id].signal.connect(lambda cv_img: self.render(id, cv_img))
                self.video_stream[id].video_path = file_path
                self.video_stream[id].cap = cv2.VideoCapture(self.video_stream[id].video_path)
                self.video_stream[id].mask = cv2.imread("mask.png")
                self.show_thumbnail(id)
            else:
                QMessageBox.warning(self, "Warning", "Please select a video file")
    def show_thumbnail(self, id):
        cap = cv2.VideoCapture(self.video_stream[id].video_path)
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame.shape
            bytes_per_line = channel * width
            q_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)
            q_pixmap = QPixmap.fromImage(q_image)
            self.ui_app.__getattribute__(f"labelVideo{id}").setPixmap(q_pixmap)
        cap.release()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = App()
    window.show()

    sys.exit(app.exec_())