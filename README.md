# Tomato Detection System

Hệ thống nhận diện và đếm số lượng cà chua sử dụng mô hình YOLO và giao diện Streamlit.

## Giới thiệu

Dự án được xây dựng nhằm hỗ trợ phát hiện và thống kê số lượng cà chua từ hình ảnh và video. Hệ thống sử dụng mô hình học sâu YOLO để nhận diện đối tượng và thực hiện đếm tự động trong vùng quan tâm được xác định trước.

## Chức năng

### Nhận diện ảnh

* Tải ảnh từ máy tính.
* Phát hiện cà chua trong ảnh.
* Hiển thị kết quả nhận diện.
* Thống kê tổng số lượng cà chua.

### Nhận diện video

* Phân tích video bằng mô hình YOLO.
* Theo dõi đối tượng (Object Tracking).
* Đếm số lượng cà chua đi vào vùng đếm.
* Hiển thị kết quả theo thời gian thực.

## Công nghệ sử dụng

* Python 3.10+
* YOLO (Ultralytics)
* OpenCV
* NumPy
* Streamlit

## Cấu trúc thư mục

```text
object_counter_app/
│
├── main.py
│
├── src/
│   ├── core/
│   │   ├── model_loader.py
│   │   ├── image_detector.py
│   │   └── video_detector.py
│   │
│   └── ui/
│       ├── main_window.py
│       ├── image_page.py
│       └── video_page.py
│
├── assets/
│   └── test.mp4
│
├── models/
│   └── best_v1.pt
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Cài đặt

### 1. Clone dự án

```bash
git clone <repository-url>
cd object_counter_app
```

### 2. Tạo môi trường ảo

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Cài đặt thư viện

```bash
pip install -r requirements.txt
```

## Mô hình

Đặt file mô hình vào thư mục:

```text
models/
└── best_v1.pt
```

## Chạy chương trình

```bash
python main.py
```

Sau khi chạy thành công, giao diện web sẽ tự động mở trên trình duyệt.

## Vùng đếm

Vùng đếm hiện được cấu hình trực tiếp trong file:

```text
src/core/video_detector.py
```

Ví dụ:

```python
self.count_polygon = np.array([
    [544, 399],
    [1563, 225],
    [1830, 730],
    [1137, 982]
], np.int32)
```

Có thể thay đổi các tọa độ này để phù hợp với từng video khác nhau.

## Kết quả

* Nhận diện đối tượng theo thời gian thực.
* Hiển thị vùng đếm trên video.
* Đếm chính xác số lượng đối tượng đi vào vùng đếm.
* Giao diện trực quan bằng Streamlit.

## Thành viên phát triển

* Nhóm phát triển dự án Tomato Detection System

## Giấy phép

Dự án được sử dụng cho mục đích học tập, nghiên cứu và phát triển.
