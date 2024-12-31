import cv2

def loopVideo(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print('Video open failed')
        return
    fps = cap.get(cv2.CAP_PROP_FPS)
    delay = int(1000 / fps)
    cv2.namedWindow('video', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    while True:
        ret, frame = cap.read()
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue
        cv2.imshow("video", frame)
        key = cv2.waitKey(delay) & 0xFF
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    loopVideo('0.mp4')
