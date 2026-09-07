import subprocess
import sys

if __name__ == "__main__":
    # 启动Streamlit应用
    subprocess.run([sys.executable, "-m", "streamlit", "run", "streamlit_app.py", "--server.port=8501"])
