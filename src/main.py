import cv2


def main():
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('Webcam', flags=cv2.WINDOW_GUI_NORMAL)
    while True:
        ret, frame = cap.read()

        cv2.imshow('Webcam', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
