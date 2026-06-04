from ultralytics import YOLO

class ModelLoader:

    def __init__(self):
        self.model = YOLO("models/best_v1.pt")

    def get_model(self):
        return self.model