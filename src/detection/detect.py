from ultralytics import YOLO

model = YOLO("models/best_v1.pt")


def detect_tomatoes(source):
    results = model(source)

    detections = []

    for result in results:
        for box in result.boxes:
            detections.append(box)

    return results[0], detections