import cv2

from .webcam import Webcam


def main():
    camera = Webcam("Webcam")
    while True:
        cv2.imshow(camera.getWindowName(), camera.getFrame())
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
