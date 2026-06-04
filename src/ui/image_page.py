import cv2
import tempfile
import streamlit as st

from src.core.image_detector import ImageDetector


def render(model):

    st.subheader("Phân tích ảnh")

    uploaded_image = st.file_uploader(
        "Chọn ảnh cần phân tích",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_image:

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".jpg"
        ) as tmp:

            tmp.write(uploaded_image.read())
            image_path = tmp.name

        detector = ImageDetector(model)

        result_image, count = detector.detect(
            image_path
        )

        result_image = cv2.cvtColor(
            result_image,
            cv2.COLOR_BGR2RGB
        )

        col1, col2 = st.columns([4, 1])

        with col1:

            st.image(
                result_image,
                caption="Kết quả nhận diện",
                use_container_width=True
            )

        with col2:

            st.metric(
                label="Tổng số cà chua",
                value=count
            )