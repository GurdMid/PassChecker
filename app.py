import webview
import threading
import streamlit.web.cli as stcli
import sys
import time
import subprocess
import os

def run_streamlit():
    # Используем subprocess для более надежного запуска
    subprocess.Popen(
        [sys.executable, "-m", "streamlit", "run", "passwordCheck.py", "--server.port", "8501"],
        creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0
    )

if __name__ == "__main__":
    print("Запуск Streamlit сервера...")
    run_streamlit()
    
    print("Ожидание загрузки сервера (5 секунд)...")
    time.sleep(5)
    
    print("Открытие окна приложения...")
    webview.create_window(
        "Проверка пароля", 
        "http://localhost:8501", 
        width=800, 
        height=600,
        resizable=True,
        confirm_close=True
    )
    webview.start()