import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

import streamlit as st

from src.core.model_loader import ModelLoader
from src.ui.image_page import render as image_page
from src.ui.video_page import render as video_page


# ==================================================
# CẤU HÌNH TRANG
# ==================================================
st.set_page_config(
    page_title="Hệ thống nhận diện cà chua",
    page_icon="🍅",
    layout="wide"
)

# ==================================================
# CSS GIAO DIỆN (MINIMAL CLEAN UI)
# ==================================================
st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.big-title {
    font-size: 42px;
    font-weight: bold;
    color: #ff4b4b;
}

.sub-title {
    color: #666;
    font-size: 18px;
    margin-bottom: 30px;
}

.block-container {
    padding-top: 2rem;
}

/* ===== FILE UPLOADER CLEAN STYLE ===== */
section[data-testid="stFileUploaderDropzone"] {
    border: 1.5px solid #e5e5e5 !important;
    border-radius: 12px !important;
    padding: 18px !important;
    background: #fafafa !important;
}

/* Text */
section[data-testid="stFileUploaderDropzone"] label {
    font-size: 15px !important;
    font-weight: 500 !important;
    color: #444 !important;
}

/* Icon */
section[data-testid="stFileUploaderDropzone"] svg {
    fill: #666 !important;
}

/* Remove inner border */
section[data-testid="stFileUploaderDropzone"] > div {
    border: none !important;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# TIÊU ĐỀ
# ==================================================
st.markdown(
    """
    <div class="big-title">
        HỆ THỐNG NHẬN DIỆN VÀ ĐẾM CÀ CHUA
    </div>

    <div class="sub-title">
        Ứng dụng AI phát hiện và đếm số lượng cà chua
    </div>
    """,
    unsafe_allow_html=True
)

# ==================================================
# LOAD MODEL
# ==================================================
@st.cache_resource
def load_model():
    return ModelLoader().get_model()

model = load_model()

# ==================================================
# TAB CHỨC NĂNG
# ==================================================
tab1, tab2 = st.tabs([
    "Nhận diện ảnh",
    "Nhận diện video"
])

# ==================================================
# NHẬN DIỆN ẢNH
# ==================================================
with tab1:
    image_page(model)

# ==================================================
# NHẬN DIỆN VIDEO
# ==================================================
with tab2:
    video_page(model)