# memory_bridge.py

import json
import os
from datetime import datetime


class MemoryBridge:

    def __init__(self):

        self.memory_file = "screen_memory.json"

        self._initialize_memory()

    # =====================================
    # Create memory file if not exists
    # =====================================

    def _initialize_memory(self):

        try:

            if not os.path.exists(self.memory_file):

                with open(
                    self.memory_file,
                    "w",
                    encoding="utf-8"
                ) as f:

                    json.dump(
                        [],
                        f,
                        indent=4
                    )

        except Exception as e:

            print(
                f"[Memory Init Error] {e}"
            )

    # =====================================
    # Load Memory Safely
    # =====================================

    def _load_memory(self):

        try:

            with open(
                self.memory_file,
                "r",
                encoding="utf-8"
            ) as f:

                return json.load(f)

        except:

            return []

    # =====================================
    # Save Memory Safely
    # =====================================

    def _save_memory(self, data):

        try:

            with open(
                self.memory_file,
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    data,
                    f,
                    indent=4,
                    ensure_ascii=False
                )

            return True

        except Exception as e:

            print(
                f"[Memory Save Error] {e}"
            )

            return False

    # =====================================
    # Store Event
    # =====================================

    def store_event(
        self,
        app,
        title,
        context,
        source="screen_intelligence"
    ):

        if not app:
            return False

        event = {

            "timestamp": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "source": source,

            "app": app,

            "title": title,

            "context": context
        }

        try:

            data = self._load_memory()

            data.append(event)

            return self._save_memory(data)

        except Exception as e:

            print(
                f"[Memory Error] {e}"
            )

            return False

    # =====================================
    # Recent Events
    # =====================================

    def get_recent_events(
        self,
        limit=10
    ):

        try:

            data = self._load_memory()

            return data[-limit:]

        except:

            return []

    # =====================================
    # Context Summary
    # =====================================

    def get_context_summary(self):

        try:

            data = self._load_memory()

            summary = {}

            for item in data:

                context = item.get(
                    "context",
                    "unknown"
                )

                summary[context] = (
                    summary.get(
                        context,
                        0
                    ) + 1
                )

            return summary

        except:

            return {}

    # =====================================
    # Total Events
    # =====================================

    def total_events(self):

        try:

            data = self._load_memory()

            return len(data)

        except:

            return 0

    # =====================================
    # Memory Information
    # =====================================

    def memory_info(self):

        return {

            "memory_file":
            self.memory_file,

            "total_events":
            self.total_events(),

            "contexts":
            self.get_context_summary()
        }

    # =====================================
    # Clear Memory
    # =====================================

    def clear_memory(self):

        try:

            self._save_memory([])

            return True

        except:

            return False


# =========================================
# TEST
# =========================================

if __name__ == "__main__":

    memory = MemoryBridge()

    memory.store_event(

        app="Code.exe",

        title="Artery Project",

        context="artery_development"
    )

    print("\nRecent Events:\n")

    print(
        memory.get_recent_events()
    )

    print("\nContext Summary:\n")

    print(
        memory.get_context_summary()
    )

    print("\nMemory Info:\n")

    print(
        memory.memory_info()
    )