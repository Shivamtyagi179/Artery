import time
from datetime import datetime

from system_monitor.memory_bridge import MemoryBridge
from system_monitor.tracker import ScreenTracker
from system_monitor.analyzer import ScreenAnalyzer
from system_monitor.controller import ScreenController


class ScreenIntelligence:

    def __init__(self, brain=None):

        self.tracker = ScreenTracker()
        self.analyzer = ScreenAnalyzer()
        self.controller = ScreenController()
        self.memory = MemoryBridge()

        self.brain = brain

        self.last_context = None
        self.last_app = None
        self.last_title = None

        self.start_time = time.time()

    # ==================================================
    # OBSERVE
    # ==================================================

    def observe(self):

        return self.tracker.get_active_window()

    # ==================================================
    # UNDERSTAND
    # ==================================================

    def understand(self, screen_data):

        return self.analyzer.detect_context(
            screen_data.get("app", ""),
            screen_data.get("title", "")
        )

    # ==================================================
    # PROCESS
    # ==================================================

    def process(self):

        screen_data = self.observe()

        context = self.understand(screen_data)

        return {
            "screen": screen_data,
            "context": context
        }

    # ==================================================
    # FORMAT TIME
    # ==================================================

    def format_runtime(self, seconds):

        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60

        return f"{hours:02}:{minutes:02}:{secs:02}"

    # ==================================================
    # DASHBOARD
    # ==================================================

    def show_dashboard(
        self,
        app,
        title,
        context
    ):

        current_time = datetime.now().strftime(
            "%H:%M:%S"
        )

        uptime = int(
            time.time()
            -
            self.start_time
        )

        runtime = self.format_runtime(
            uptime
        )

        brain_status = (
            "CONNECTED"
            if self.brain
            else "OFFLINE"
        )

        usage = self.tracker.get_system_usage()
        tracker_state = self.tracker.get_tracker_state() or {}

        mouse_active = tracker_state.get("mouse_active", False)

        keyboard_active = tracker_state.get("keyboard_active", False)

        idle_time = tracker_state.get("idle_time", 0)

        user_idle = tracker_state.get("user_idle", False)

        user_status = (
            "IDLE"
            if user_idle
            else "ACTIVE"
        )
        running_apps = (
            self.tracker.get_running_apps()
        )

        app_changes = (
            self.tracker.detect_app_changes()
        )

        print()

        print(
            "╔══════════════════════════════════════════════════════════════╗"
        )

        print(
            "║               🧠 ARTERY SCREEN INTELLIGENCE v2             ║"
        )

        print(
            "╠══════════════════════════════════════════════════════════════╣"
        )

        print(
            f"║ 🕒 Time           : {current_time:<38}║"
        )

        print(
            f"║ 🖥 Active App     : {app[:38]:<38}║"
        )

        print(
            f"║ 🎯 Context        : {context[:38]:<38}║"
        )

        print(
            f"║ 🔗 Brain Status   : {brain_status:<38}║"
        )

        print(
            f"║ 💾 Memory Status  : {'ACTIVE':<38}║"
        )

        print(
            f"║ ⏱ Runtime        : {runtime:<38}║"
        )

        print(
            f"║ 🖥 CPU Usage      : {str(usage['cpu'])+' %':<38}║"
        )

        print(
            f"║ 💾 RAM Usage      : {str(usage['ram'])+' %':<38}║"
        )

        print(
            f"║ 📦 Running Apps   : {str(len(running_apps)):<38}║"
        )

        print(
            f"║ 🖱 Mouse Active   : {str(mouse_active):<38}║"
       )

        print(
            f"║ ⌨ Keyboard Act. : {str(keyboard_active):<38}║"
        )  

        print(
            f"║ 😴 Idle Time     : {str(idle_time)+' sec':<38}║"
   )

        print(
            f"║ 👤 User Status   : {user_status:<38}║"
     )

        print(
            "╠══════════════════════════════════════════════════════════════╣"
        )

        print(
            "║ 📄 ACTIVE WINDOW                                           ║"
        )

        print(
            "╠══════════════════════════════════════════════════════════════╣"
        )

        title = (
            title[:55] + "..."
            if len(title) > 55
            else title
        )

        print(
            f"║ {title:<60}║"
        )

        print(
            "╠══════════════════════════════════════════════════════════════╣"
        )

        print(
            "║ ⚡ RECENT APP EVENTS                                        ║"
        )

        print(
            "╠══════════════════════════════════════════════════════════════╣"
        )

        if app_changes["new"]:

            for app_name in app_changes["new"][:3]:

                app_name = app_name[:48]

                print(
                    f"║ ➕ Opened : {app_name:<47}║"
                )

        if app_changes["closed"]:

            for app_name in app_changes["closed"][:3]:

                app_name = app_name[:48]

                print(
                    f"║ ➖ Closed : {app_name:<47}║"
                )

        if (
            not app_changes["new"]
            and
            not app_changes["closed"]
        ):

            print(
                "║ No recent application events                               ║"
            )

        print(
            "╠══════════════════════════════════════════════════════════════╣"
        )

        print(
            "║ 🚀 ACTIVE CAPABILITIES                                     ║"
        )

        print(
            "║    • Active Window Detection                               ║"
        )

        print(
            "║    • Running Apps Detection                                ║"
        )

        print(
            "║    • Context Detection                                     ║"
        )

        print(
            "║    • CPU Monitoring                                        ║"
        )

        print(
            "║    • RAM Monitoring                                        ║"
        )

        print(
            "║    • App Launch Detection                                  ║"
        )

        print(
            "║    • App Close Detection                                   ║"
        )

        print(
            "║    • Brain Synchronization                                 ║"
        )

        print(
            "║    • Memory Logging                                        ║"
        )

        print(
            "╚══════════════════════════════════════════════════════════════╝"
        )

    # ==================================================
    # MONITOR
    # ==================================================

    def monitor(self):

        print("\n")

        print(
            "=============================================================="
        )

        print(
            "🧠 ARTERY SCREEN INTELLIGENCE INITIALIZED"
        )

        print(
            "👁 Visual Monitoring Active"
        )

        print(
            "🖥 Running App Monitoring Active"
        )

        print(
            "📊 CPU & RAM Monitoring Active"
        )

        print(
            "🔗 Brain Connection Ready"
        )

        print(
            "💾 Memory Logging Enabled"
        )
        print(
            "🖱 Mouse Tracking Active"
        )

        print(
            "⌨ Keyboard Tracking Active"
        )

        print(
             "😴 Idle Detection Active"
        ) 

        print(
            "=============================================================="
        )

        while True:

            try:

                result = self.process()

                screen = result.get(
                    "screen",
                    {}
                )

                app = screen.get(
                    "app"
                )

                title = screen.get(
                    "title"
                ) or ""

                context = result.get(
                    "context"
                ) or ""

                if not app:

                    time.sleep(1)

                    continue

                changed = (

                    app != self.last_app

                    or

                    title != self.last_title

                    or

                    context != self.last_context
                )

                if changed:

                    self.memory.store_event(
                        app,
                        title,
                        context
                    )

                    tracker_state = self.tracker.get_tracker_state() or {}

                    event = {
                        "source": "screen_intelligence",
                        "app": app,
                        "title": title,
                        "context": context,
                        "cpu": tracker_state.get("cpu"),
                        "ram": tracker_state.get("ram"),
                        "running_apps": tracker_state.get("running_apps"),
                        "mouse_active": tracker_state.get("mouse_active"),
                        "keyboard_active": tracker_state.get("keyboard_active"),
                        "idle_time": tracker_state.get("idle_time"),
                        "user_idle": tracker_state.get("user_idle")
                    }

                    if (
                        self.brain
                        and hasattr(
                            self.brain,
                            "receive_event"
                        )
                    ):

                        self.brain.receive_event(
                            event
                        )

                    self.show_dashboard(
                        app,
                        title,
                        context
                    )

                    self.last_app = app
                    self.last_title = title
                    self.last_context = context

                time.sleep(1)

            except Exception as e:

                print(
                    f"\n[Screen Intelligence Error] {e}"
                )

                time.sleep(2)


if __name__ == "__main__":

    si = ScreenIntelligence()

    si.monitor()