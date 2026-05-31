# Tomato Detection System (YOLOv8)

## 1. Giới thiệu
Đây là dự án nhận diện cà chua sử dụng mô hình YOLOv8 kết hợp giao diện desktop bằng Python (CustomTkinter).

Hệ thống có các chức năng:
- Nhận diện cà chua trong ảnh
- Nhận diện cà chua trong video
- Hiển thị kết quả bằng bounding box
- Phát triển thêm chức năng đếm số lượng cà chua

---

## 2. Công nghệ sử dụng
- Python
- YOLOv8 (Ultralytics)
- OpenCV
- CustomTkinter
- Pillow
- NumPy

---

## 3. Cấu trúc thư mục
tomato-detection-system/
│
├── models/
│ └── best.pt
│
├── src/
│ ├── detection/
│ ├── counting/
│ └── ui/
│
├── main.py
├── requirements.txt
└── README.md

---

