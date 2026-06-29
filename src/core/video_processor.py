import cv2
from ultralytics import solutions


class VideoProcessor:
    def __init__(self, video_path, model_path="models/best_v1.pt"):
        self.cap = cv2.VideoCapture(video_path)
        assert self.cap.isOpened(), "Cannot open video"

        self.region_points =[[542,   3],
 [582 , 36],
 [580 ,125],
 [229 ,212],
 [230 , 77],
 [186 , 22]]

        self.counter = solutions.ObjectCounter(
            show=False,
            region=self.region_points,
            model=model_path,
        )

    def read_frame(self):
        success, frame = self.cap.read()
        if not success:
            return None

        results = self.counter(frame)
        return results.plot_im

    def release(self):
        self.cap.release()