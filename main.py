import cv2
from cv2 import VideoWriter


def saveWebcamOutput(path):
    cap = cv2.VideoCapture(0)
    width = int(cap.get(3))
    height = int(cap.get(4))
    size = (width, height)
    codec = cv2.VideoWriter_fourcc(*'mp4v')
    result = cv2.VideoWriter(path, codec, 30, size)
    while (True):
        ret, frame = cap.read()
        result.write(frame)
        # The original input frame is shown in the window
        cv2.imshow('Original', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    # After we release our webcam, we also release the output
    result.release()
    # De-allocate any associated memory usage
    cv2.destroyAllWindows()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    saveWebcamOutput("./Result/output.mp4")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
