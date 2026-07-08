import cv2


class Webcam:
    def __init__(self, window_name: str):
        self.cap = cv2.VideoCapture(0)
        self.window_name = window_name
        cv2.namedWindow(window_name, flags=cv2.WINDOW_GUI_NORMAL)

    def getFrame(self):
        ret, frame = self.cap.read()
        return frame

    def release(self):
        self.cap.release()

    def getWindowName(self):
        return self.window_name
