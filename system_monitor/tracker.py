# tracker.py

import time
import psutil
import pyautogui
import keyboard
import win32gui
import win32process

from datetime import datetime


class ScreenTracker:

    def __init__(self):

        self.last_window = None

        self.session_start = time.time()

        self.previous_apps = set(
            self.get_running_apps()
        )

        self.last_mouse_position = (
            pyautogui.position()
        )

        self.last_activity_time = (
            time.time()
        )

        self.last_keyboard_time = (
            time.time()
        )

        self.last_mouse_time = (
            time.time()
        )

    # ==================================================
    # ACTIVE WINDOW
    # ==================================================

    def get_active_window(self):

        try:

            hwnd = win32gui.GetForegroundWindow()

            title = win32gui.GetWindowText(hwnd)

            _, pid = (
                win32process
                .GetWindowThreadProcessId(hwnd)
            )

            process = psutil.Process(pid)

            process_name = process.name()

            return {

                "timestamp":
                datetime.now().strftime(
                    "%H:%M:%S"
                ),

                "title":
                title,

                "app":
                process_name,

                "pid":
                pid
            }

        except Exception as e:

            return {
                "error": str(e)
            }

    # ==================================================
    # WINDOW CHANGE
    # ==================================================

    def has_changed(
        self,
        current_window
    ):

        if current_window != self.last_window:

            self.last_window = current_window

            self.session_start = (
                time.time()
            )

            return True

        return False

    # ==================================================
    # SESSION
    # ==================================================

    def get_session_duration(self):

        return round(

            time.time()
            -
            self.session_start,

            1
        )

    # ==================================================
    # RUNNING APPS
    # ==================================================

    def get_running_apps(self):

        apps = set()

        try:

            for proc in psutil.process_iter(
                ["name"]
            ):

                name = proc.info.get(
                    "name"
                )

                if name:

                    apps.add(name)

        except:
            pass

        return sorted(
            list(apps)
        )

    # ==================================================
    # APP CHANGES
    # ==================================================

    def detect_app_changes(self):

        current_apps = set(
            self.get_running_apps()
        )

        new_apps = (
            current_apps
            -
            self.previous_apps
        )

        closed_apps = (
            self.previous_apps
            -
            current_apps
        )

        self.previous_apps = current_apps

        return {

            "new":
            list(new_apps),

            "closed":
            list(closed_apps)
        }

    # ==================================================
    # SYSTEM USAGE
    # ==================================================

    def get_system_usage(self):

        return {

            "cpu":
            psutil.cpu_percent(),

            "ram":
            psutil.virtual_memory().percent
        }

    # ==================================================
    # MOUSE ACTIVITY
    # ==================================================

    def get_mouse_activity(self):

        try:

            current_pos = (
                pyautogui.position()
            )

            active = (

                current_pos
                !=
                self.last_mouse_position

            )

            if active:

                self.last_mouse_position = (
                    current_pos
                )

                self.last_mouse_time = (
                    time.time()
                )

                self.last_activity_time = (
                    time.time()
                )

            return {

                "active":
                active,

                "position":
                current_pos
            }

        except:

            return {

                "active":
                False,

                "position":
                (0, 0)
            }

    # ==================================================
    # KEYBOARD ACTIVITY
    # ==================================================

    def get_keyboard_activity(self):

        active = False

        try:

            keys = [

                "shift",
                "ctrl",
                "alt",
                "space",
                "enter"
            ]

            for key in keys:

                if keyboard.is_pressed(
                    key
                ):

                    active = True

                    break

            if active:

                self.last_keyboard_time = (
                    time.time()
                )

                self.last_activity_time = (
                    time.time()
                )

        except:
            pass

        return active

    # ==================================================
    # IDLE TIME
    # ==================================================

    def get_idle_time(self):

        return round(

            time.time()
            -
            self.last_activity_time,

            1
        )

    # ==================================================
    # USER IDLE
    # ==================================================

    def is_user_idle(self):

        return (

            self.get_idle_time()
            >
            60
        )

    # ==================================================
    # TRACKER STATE
    # ==================================================

    def get_tracker_state(self):

        usage = (
            self.get_system_usage()
        )

        mouse = (
            self.get_mouse_activity()
        )

        keyboard_active = (
            self.get_keyboard_activity()
        )

        return {

            "cpu":
            usage["cpu"],

            "ram":
            usage["ram"],

            "running_apps":
            len(
                self.get_running_apps()
            ),

            "mouse_active":
            mouse["active"],

            "mouse_position":
            str(
                mouse["position"]
            ),

            "keyboard_active":
            keyboard_active,

            "idle_time":
            self.get_idle_time(),

            "user_idle":
            self.is_user_idle()
        }

    # ==================================================
    # DASHBOARD
    # ==================================================

    def print_status(
        self,
        data
    ):

        usage = (
            self.get_system_usage()
        )

        apps = (
            self.get_running_apps()
        )

        changes = (
            self.detect_app_changes()
        )

        tracker_state = (
            self.get_tracker_state()
        )

        print()

        print(
            "╔══════════════════════════════════════════════════════════════╗"
        )

        print(
            "║          🧠 ARTERY ULTIMATE SCREEN TRACKER                 ║"
        )

        print(
            "╠══════════════════════════════════════════════════════════════╣"
        )

        print(
            f"║ ⏰ Time       : {data.get('timestamp',''):<42}║"
        )

        print(
            f"║ 📦 App        : {data.get('app',''):<42}║"
        )

        print(
            f"║ 🆔 PID        : {str(data.get('pid','')):<42}║"
        )

        print(
            f"║ ⌛ Session    : {str(self.get_session_duration())+' sec':<42}║"
        )

        print(
            f"║ 🖥 CPU Usage  : {str(usage['cpu'])+' %':<42}║"
        )

        print(
            f"║ 💾 RAM Usage  : {str(usage['ram'])+' %':<42}║"
        )

        print(
            f"║ 🖱 Mouse      : {str(tracker_state['mouse_active']):<42}║"
        )

        print(
            f"║ ⌨ Keyboard   : {str(tracker_state['keyboard_active']):<42}║"
        )

        print(
            f"║ 😴 Idle Time : {str(tracker_state['idle_time'])+' sec':<42}║"
        )

        print(
            "╠══════════════════════════════════════════════════════════════╣"
        )

        title = data.get(
            "title",
            ""
        )

        if len(title) > 55:

            title = (
                title[:55]
                +
                "..."
            )

        print(
            f"║ 📄 {title:<56}║"
        )

        print(
            "╠══════════════════════════════════════════════════════════════╣"
        )

        print(
            f"║ 🟢 Running Apps : {len(apps):<41}║"
        )

        print(
            "╚══════════════════════════════════════════════════════════════╝"
        )


# ==================================================
# TEST
# ==================================================

if __name__ == "__main__":

    tracker = ScreenTracker()

    print(
        "\n🚀 Artery Ultimate Screen Tracker Started...\n"
    )

    while True:

        current = (
            tracker.get_active_window()
        )

        if tracker.has_changed(
            current
        ):

            tracker.print_status(
                current
            )

        time.sleep(1)