import subprocess
import sys

subprocess.run(
    [
        sys.executable,
        "-m",
        "streamlit",
        "run",
        "src/ui/main_window.py"
    ]
)