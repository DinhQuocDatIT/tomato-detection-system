import cv2
from collections import Counter


class ImageDetector:
    def __init__(self, model):
        """
        model: YOLO model (ultralytics)
        """
        self.model = model

    def detect(self, image_path):
        """
        Detect cà chua trong ảnh và trả về:
        - ảnh đã annotate
        - thống kê số lượng từng loại
        - confidence trung bình theo class
        - tỷ lệ phần trăm từng loại
        - quyết định tổng thể
        """

        # ======================
        # 1. LOAD IMAGE
        # ======================
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"❌ Không đọc được ảnh: {image_path}")

        # ======================
        # 2. INFERENCE MODEL
        # ======================
        results = self.model(image)
        result = results[0]

        # ảnh đã vẽ bounding box
        annotated_image = result.plot()

        # tên class từ model
        names = self.model.names

        # ======================
        # 3. EXTRACT PREDICTIONS
        # ======================
        classes = []
        confidences = []

        if result.boxes is not None and len(result.boxes) > 0:
            for box in result.boxes:
                cls_id = int(box.cls[0])
                conf = float(box.conf[0])

                class_name = names[cls_id]

                classes.append(class_name)
                confidences.append(conf)

        # ======================
        # 4. COUNT CLASSES
        # ======================
        counter = Counter(classes)

        # ======================
        # 5. CONFIDENCE AVG PER CLASS
        # ======================
        conf_map = {}
        for c, conf in zip(classes, confidences):
            conf_map.setdefault(c, []).append(conf)

        avg_conf = {
            k: round(sum(v) / len(v), 3)
            for k, v in conf_map.items()
        }

        # ======================
        # 6. RATIO (%)
        # ======================
        total = sum(counter.values())

        ratio = {
            k: round((v / total) * 100, 2)
            for k, v in counter.items()
        } if total > 0 else {}

        # ======================
        # 7. DECISION LOGIC
        # ======================
        # normalize keys to avoid case mismatch
        keys_lower = [k.lower() for k in counter.keys()]

        has_bad = any("bad" in k or "hư" in k for k in keys_lower)

        good_count = counter.get("good", 0) + counter.get("chín", 0)
        good_ratio = good_count / total if total > 0 else 0

        if has_bad:
            decision = "❌ BATCH KHÔNG ĐẠT - Phát hiện trái hư"
        elif good_ratio > 0.7:
            decision = "✔ BATCH ĐẠT - Có thể thu hoạch"
        else:
            decision = "⚠ BATCH TRUNG BÌNH - Cần phân loại thêm"

        # ======================
        # 8. RETURN
        # ======================
        return annotated_image, counter, avg_conf, ratio, decision