import customtkinter as ctk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
import threading

from src.detection.detect import detect_tomatoes
from src.counting.counter import count_tomatoes


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Tomato Detection System")
        self.geometry("1000x700")

        # ===== UI =====
        self.btn_image = ctk.CTkButton(self, text="Chọn Ảnh", command=self.load_image)
        self.btn_image.pack(pady=10)

        self.btn_video = ctk.CTkButton(self, text="Chọn Video", command=self.load_video)
        self.btn_video.pack(pady=10)

        self.video_label = ctk.CTkLabel(self, text="")
        self.video_label.pack()

        self.result_label = ctk.CTkLabel(self, text="Số lượng cà chua: 0")
        self.result_label.pack(pady=10)

        self.image_label = ctk.CTkLabel(self, text="")
        self.image_label.pack()

        self.cap = None
        self.running = False

    # ================= IMAGE =================
    def load_image(self):
        file_path = filedialog.askopenfilename()

        if file_path:
            result, detections = detect_tomatoes(file_path)

            total = count_tomatoes(detections)
            self.result_label.configure(text=f"Số lượng cà chua: {total}")

            img = result.plot()
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            img = Image.fromarray(img)
            img = ImageTk.PhotoImage(img)

            self.image_label.configure(image=img)
            self.image_label.image = img

    # ================= VIDEO =================
    def load_video(self):
        file_path = filedialog.askopenfilename()

        if file_path:
            self.cap = cv2.VideoCapture(file_path)
            self.running = True

            threading.Thread(target=self.play_video, daemon=True).start()

    def play_video(self):
        while self.running and self.cap.isOpened():

            ret, frame = self.cap.read()
            if not ret:
                break

            result, detections = detect_tomatoes(frame)

            total = count_tomatoes(detections)
            self.result_label.configure(text=f"Số lượng cà chua: {total}")

            frame = result.plot()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            img = Image.fromarray(frame)
            img = ImageTk.PhotoImage(img)

            self.video_label.configure(image=img)
            self.video_label.image = img

        self.cap.release()