import cv2
import tempfile
import streamlit as st

from src.core.image_detector import ImageDetector


def render(model):

    st.subheader("🍅 Nhận diện & Phân tích cà chua AI")

    uploaded_image = st.file_uploader(
        "Chọn ảnh cà chua",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_image:

        # =========================
        # 1. SAVE TEMP IMAGE
        # =========================
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
            tmp.write(uploaded_image.read())
            image_path = tmp.name

        # =========================
        # 2. LOAD ORIGINAL IMAGE
        # =========================
        original_image = cv2.imread(image_path)
        original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

        # =========================
        # 3. RUN DETECTION
        # =========================
        detector = ImageDetector(model)
        result_image, counter, avg_conf, ratio, decision = detector.detect(image_path)

        result_image = cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)

        # =========================
        # 4. SHOW IMAGES
        # =========================
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Ảnh gốc")
            st.image(original_image, use_container_width=True)

        with col2:
            st.markdown("### Kết quả AI")
            st.image(result_image, use_container_width=True)

        st.markdown("---")

        # =========================
        # 6. CLASS DETAILS
        # =========================
        st.markdown("### 🍅 Chi tiết phân loại")

        for k, v in counter.items():

            key = k.lower()
            conf = avg_conf.get(k, 0)
            percent = ratio.get(k, 0)

            if "good" in key or "ngon" in key or "chín" in key:
                icon = "🍅"
                color = "#2ecc71"

            elif "unripe" in key or "green" in key:
                icon = "🟡"
                color = "#f1c40f"

            elif "bad" in key or "hư" in key:
                icon = "❌"
                color = "#e74c3c"

            else:
                icon = "🔵"
                color = "#3498db"

            st.markdown(
                f"""
                {icon} <span style='color:{color}; font-weight:600'>{k}</span>  
                - Số lượng: <b>{v}</b>  
                - Tỷ lệ: <b>{percent:.2f}%</b>  
                - Độ tin cậy TB: <b>{conf:.3f}</b>
                """,
                unsafe_allow_html=True
            )

        st.markdown("---")

       