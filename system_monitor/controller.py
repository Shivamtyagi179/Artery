# controller.py

import pyautogui
import pygetwindow as gw
import time


class ScreenController:

    def __init__(self):

        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.2

    # ========================
    # Mouse Controls
    # ========================

    def move_mouse(self, x, y, duration=0.3):
        pyautogui.moveTo(x, y, duration=duration)

    def click(self, x=None, y=None):
        pyautogui.click(x=x, y=y)

    def double_click(self, x=None, y=None):
        pyautogui.doubleClick(x=x, y=y)

    def right_click(self, x=None, y=None):
        pyautogui.rightClick(x=x, y=y)

    def drag(self, start_x, start_y, end_x, end_y):
        pyautogui.moveTo(start_x, start_y)
        pyautogui.dragTo(end_x, end_y, duration=0.5)

    # ========================
    # Keyboard Controls
    # ========================

    def type_text(self, text):
        pyautogui.write(text, interval=0.02)

    def press_key(self, key):
        pyautogui.press(key)

    def hotkey(self, *keys):
        pyautogui.hotkey(*keys)

    # ========================
    # Scroll Controls
    # ========================

    def scroll_up(self, amount=500):
        pyautogui.scroll(amount)

    def scroll_down(self, amount=500):
        pyautogui.scroll(-amount)

    # ========================
    # Window Controls
    # ========================

    def maximize_window(self):

        try:
            window = gw.getActiveWindow()

            if window:
                window.maximize()

        except Exception as e:
            print(f"Error: {e}")

    def minimize_window(self):

        try:
            window = gw.getActiveWindow()

            if window:
                window.minimize()

        except Exception as e:
            print(f"Error: {e}")

    def close_window(self):

        pyautogui.hotkey("alt", "f4")

    # ========================
    # Browser Controls
    # ========================

    def new_tab(self):
        pyautogui.hotkey("ctrl", "t")

    def close_tab(self):
        pyautogui.hotkey("ctrl", "w")

    def next_tab(self):
        pyautogui.hotkey("ctrl", "tab")

    def previous_tab(self):
        pyautogui.hotkey("ctrl", "shift", "tab")

    # ========================
    # Screen Info
    # ========================

    def get_screen_size(self):

        width, height = pyautogui.size()

        return {
            "width": width,
            "height": height
        }

    def get_mouse_position(self):

        x, y = pyautogui.position()

        return {
            "x": x,
            "y": y
        }

    # ========================
    # Safety Layer
    # ========================

    def safe_click(self, x, y):

        screen = self.get_screen_size()

        if (
            0 <= x <= screen["width"]
            and
            0 <= y <= screen["height"]
        ):
            pyautogui.click(x, y)
            return True

        return False