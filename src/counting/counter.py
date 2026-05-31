def count_tomatoes(detections):
    """
    Đếm số lượng cà chua dựa trên bounding boxes
    detections: list các object detect từ YOLO
    """

    if detections is None:
        return 0

    return len(detections)