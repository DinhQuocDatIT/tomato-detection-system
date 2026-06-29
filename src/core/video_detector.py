import cv2
import numpy as np


class VideoDetector:

    def __init__(self, model):

        self.model = model

        self.count_polygon = np.array([[542,   3],
 [582 , 36],
 [580 ,125],
 [229 ,212],
 [230 , 77],
 [186 , 22]], np.int32)

        self.counted_ids = set()
        self.total_count = 0

    def detect(self, video_path):

        cap = cv2.VideoCapture(video_path)

        while True:

            ret, frame = cap.read()

            if not ret:
                break

            results = self.model.track(
                frame,
                persist=True,
                verbose=False
            )

            result = results[0]

            # YOLO tự vẽ bbox
            annotated_frame = result.plot()

            # Vẽ vùng đếm
            cv2.polylines(
                annotated_frame,
                [self.count_polygon],
                True,
                (0, 255, 255),
                3
            )

            if result.boxes.id is not None:

                boxes = result.boxes.xyxy.cpu().numpy()
                ids = result.boxes.id.cpu().numpy().astype(int)

                for box, track_id in zip(boxes, ids):

                    x1, y1, x2, y2 = box

                    cx = int((x1 + x2) / 2)
                    cy = int((y1 + y2) / 2)

                    inside = cv2.pointPolygonTest(
                        self.count_polygon,
                        (cx, cy),
                        False
                    )

                    # Màu tâm object
                    # Đỏ = trong vùng đếm
                    # Xanh = ngoài vùng đếm
                    color = (0, 255, 0)

                    if inside >= 0:
                        color = (0, 0, 255)

                    cv2.circle(
                        annotated_frame,
                        (cx, cy),
                        8,
                        color,
                        -1
                    )

                    # Đếm object
                    if inside >= 0:

                        if track_id not in self.counted_ids:

                            self.counted_ids.add(track_id)
                            self.total_count += 1

            # Khung hiển thị Count nhỏ gọn
            cv2.rectangle(
                annotated_frame,
                (20, 20),
                (180, 70),
                (0, 0, 0),
                -1
            )

            cv2.putText(
                annotated_frame,
                f"Count: {self.total_count}",
                (30, 55),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

            yield annotated_frame, self.total_count

        cap.release()