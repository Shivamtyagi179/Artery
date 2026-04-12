import subprocess
import os

def open_app(app_name):
    try:
        subprocess.Popen(app_name)
        return f"{app_name} open kar diya boss."
    except:
        return None

def close_app(app_name):
    try:
        subprocess.run(
            ["taskkill", "/f", "/t", "/im", f"{app_name}.exe"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return f"{app_name} close kar diya boss."
    except:
        return "App close nahi ho paaya boss."