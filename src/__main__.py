import cv2
import numpy as np

from .webcam import Webcam
from .stylization import Stylization


def main():
    camera = Webcam("Webcam")
    stylization = Stylization()
    stylization.setStyle("styles/picasso.jpg")
    while True:
        frame = camera.getFrame()
        frame_stylized = stylization.ApplyStyle(frame)
        frame_stylized = (frame_stylized * 255).astype(np.uint8)
        frame_stylized = cv2.cvtColor(frame_stylized, cv2.COLOR_RGB2BGR)
        cv2.imshow(camera.getWindowName(), frame_stylized)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
