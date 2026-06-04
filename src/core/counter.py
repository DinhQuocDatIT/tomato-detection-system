import cv2
import numpy as np

class ObjectCounter:

    def __init__(self, polygon_points):
        self.polygon = np.array(polygon_points, np.int32)
        self.counted_ids = set()
        self.total_count = 0

    def update(self, track_id, center_x, center_y):

        point = (int(center_x), int(center_y))

        inside = cv2.pointPolygonTest(
            self.polygon,
            point,
            False
        )

        if inside >= 0 and track_id not in self.counted_ids:
            self.counted_ids.add(track_id)
            self.total_count += 1

        return self.total_count