import cv2
import streamlit as st

from src.core.video_detector import VideoDetector


def render(model):

    st.subheader("Phân tích video")

    VIDEO_PATH = "assets/test.mp4"

    col1, col2 = st.columns([4, 1])

    video_placeholder = col1.empty()

    count_placeholder = col2.empty()

    if st.button("▶ Bắt đầu nhận diện"):

        detector = VideoDetector(model)

        for frame, count in detector.detect(
            VIDEO_PATH
        ):

            frame_rgb = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2RGB
            )

            video_placeholder.image(
                frame_rgb,
                channels="RGB",
                use_container_width=True
            )

            count_placeholder.metric(
                label="Số lượng cà chua",
                value=count
            )