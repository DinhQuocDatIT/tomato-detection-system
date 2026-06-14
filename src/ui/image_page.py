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

        # ==================================================
        # SAVE TEMP IMAGE
        # ==================================================
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
            tmp.write(uploaded_image.read())
            image_path = tmp.name

        # ==================================================
        # LOAD IMAGE GỐC
        # ==================================================
        original_image = cv2.imread(image_path)
        original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

        # ==================================================
        # DETECT
        # ==================================================
        detector = ImageDetector(model)
        result_image, count = detector.detect(image_path)

        result_image = cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)

        # ==================================================
        # UI LAYOUT ĐẸP
        # ==================================================
        col1, col2 = st.columns(2, gap="large")

        with col1:
            st.markdown("### Ảnh gốc")
            st.image(
                original_image,
                use_container_width=True
            )

        with col2:
            st.markdown("### Kết quả nhận diện")
            st.image(
                result_image,
                use_container_width=True
            )

        # ==================================================
        # METRIC (BELOW)
        # ==================================================
        st.markdown("---")

        st.metric(
            label="🍅 Tổng số cà chua phát hiện",
            value=count
        )