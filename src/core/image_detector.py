import cv2


class ImageDetector:

    def __init__(self, model):
        self.model = model

    def detect(self, image_path):

        image = cv2.imread(image_path)

        results = self.model(image)

        result = results[0]

        # YOLO tự vẽ bbox
        annotated_image = result.plot()

        count = len(result.boxes)

        return annotated_image, count