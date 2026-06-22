# modules/app_control/common_app_task.py

import subprocess
import pyautogui
import psutil
import os


class CommonAppTask:
    def __init__(self):
        print("[CommonAppTask] Ready")

        # 🔥 Local apps (path + fallback command)
        self.app_map = {
            # 🟢 BASIC WINDOWS
            "notepad": "notepad.exe",
            "calculator": "calc.exe",
            "paint": "mspaint.exe",
            "explorer": "explorer.exe",

            # 🟡 MICROSOFT OFFICE (use command fallback)
            "word": "winword",
            "excel": "excel",
            "powerpoint": "powerpnt",

            # 🔵 OPTIONAL FULL PATH (if needed)
            "word_path": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
            "excel_path": r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
            "powerpoint_path": r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"
        }

    # ================= MAIN =================
    def handle(self, cmd: str):
        cmd = cmd.lower().strip()

        # 🔹 OPEN APP
        if cmd.startswith("open "):
            app = cmd.replace("open", "").strip()
            return self.open_app(app)

        # 🔹 CLOSE APP
        if cmd.startswith("close "):
            app = cmd.replace("close", "").strip()
            return self.close_app(app)

        # 🔹 SCROLL
        if "scroll down" in cmd:
            pyautogui.scroll(-500)
            return "Scrolling down boss."

        if "scroll up" in cmd:
            pyautogui.scroll(500)
            return "Scrolling up boss."

        return None

    # ================= OPEN =================
    def open_app(self, app):
        path = self.app_map.get(app)

        if not path:
            return f"{app} app not found boss."

        # 🔹 Check running
        exe_name = self.get_exe_name(path)

        if exe_name and self.is_running(exe_name):
            return f"{app} already open boss."

        try:
            # 🔥 Try direct command first
            subprocess.Popen(path)
            return f"{app} open kar diya boss."
        except:
            # 🔥 Fallback to full path (if exists)
            alt_path = self.app_map.get(f"{app}_path")
            if alt_path and os.path.exists(alt_path):
                try:
                    subprocess.Popen(alt_path)
                    return f"{app} open via path boss."
                except Exception as e:
                    return f"Error opening {app}: {str(e)}"

            return f"{app} open nahi ho paya boss."

    # ================= CLOSE =================
    def close_app(self, app):
        path = self.app_map.get(app)

        if not path:
            return "App not found boss."

        exe_name = self.get_exe_name(path)

        if not exe_name:
            return "Close failed boss."

        try:
            subprocess.run(
                ["taskkill", "/f", "/t", "/im", exe_name],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            return f"{app} close kar diya boss."
        except Exception as e:
            return f"Error closing {app}: {str(e)}"

    # ================= HELPERS =================
    def get_exe_name(self, path):
        """Extract exe name"""
        if path.endswith(".exe"):
            return os.path.basename(path)
        else:
            return path + ".exe"

    def is_running(self, exe_name):
        for process in psutil.process_iter(['name']):
            try:
                if process.info['name'] and process.info['name'].lower() == exe_name.lower():
                    return True
            except:
                pass
        return False