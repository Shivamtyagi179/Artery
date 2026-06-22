import os
import shutil

class FileExplorerTask:
    def __init__(self):
        self.desktop = os.path.join(os.path.expanduser("~"), "Desktop")

    # ================= MAIN =================
    def handle(self, cmd: str):
        cmd = cmd.lower().strip()

        # ===== CREATE FOLDER =====
        if "create" in cmd and "folder" in cmd:
            name = cmd.replace("create", "").replace("folder", "").strip()

            if not name:
                return "Folder ka naam bolo boss."

            path = os.path.join(self.desktop, name)

            try:
                os.makedirs(path, exist_ok=True)
                os.startfile(self.desktop)
                return f"{name} folder desktop par bana diya boss."
            except:
                return "Folder create nahi ho paya boss."

        # ===== CREATE FILE =====
        if "create" in cmd and "file" in cmd:
            name = cmd.replace("create", "").replace("file", "").strip()

            if not name:
                return "File ka naam bolo boss."

            if "." not in name:
                name += ".txt"

            path = os.path.join(self.desktop, name)

            try:
                with open(path, "w") as f:
                    f.write("")
                os.startfile(self.desktop)
                return f"{name} file bana di boss."
            except:
                return "File create nahi ho payi boss."

        # ===== OPEN FOLDER IN DESKTOP =====
        if "open" in cmd and "folder" in cmd and "desktop" in cmd:
            name = cmd.replace("open", "").replace("folder", "").replace("in desktop", "").strip()

            path = os.path.join(self.desktop, name)

            if os.path.exists(path):
                os.startfile(self.desktop)
                os.startfile(path)
                return f"{name} folder open kar diya boss."
            else:
                return "Folder nahi mila boss."

        # ===== OPEN (GENERAL) =====
        if cmd.startswith("open "):
            name = cmd.replace("open", "").strip()
            path = os.path.join(self.desktop, name)

            if os.path.exists(path):
                os.startfile(path)
                return f"{name} open kar diya boss."
            return None

        # ===== DELETE =====
        if "delete" in cmd:
            name = cmd.replace("delete", "").replace("folder", "").replace("file", "").strip()
            path = os.path.join(self.desktop, name)

            if os.path.exists(path):
                try:
                    if os.path.isdir(path):
                        shutil.rmtree(path)
                    else:
                        os.remove(path)
                    return f"{name} delete ho gaya boss."
                except:
                    return "Delete nahi ho paya boss."
            return None

        # ===== RENAME =====
        if "rename" in cmd and "to" in cmd:
            try:
                parts = cmd.split("to")
                old_name = parts[0].replace("rename", "").strip()
                new_name = parts[1].strip()

                old_path = os.path.join(self.desktop, old_name)
                new_path = os.path.join(self.desktop, new_name)

                if os.path.exists(old_path):
                    os.rename(old_path, new_path)
                    return f"{old_name} rename karke {new_name} kar diya boss."
                else:
                    return "File ya folder nahi mila boss."
            except:
                return "Rename nahi ho paya boss."

        # ===== MOVE =====
        if "move" in cmd and "to" in cmd:
            try:
                parts = cmd.split("to")
                name = parts[0].replace("move", "").strip()
                folder = parts[1].strip()

                src = os.path.join(self.desktop, name)
                dest = os.path.join(self.desktop, folder)

                if os.path.exists(src) and os.path.exists(dest):
                    shutil.move(src, dest)
                    return f"{name} move ho gaya boss."
                else:
                    return "File ya folder nahi mila boss."
            except:
                return "Move nahi ho paya boss."

        # ===== COPY =====
        if "copy" in cmd and "to" in cmd:
            try:
                parts = cmd.split("to")
                name = parts[0].replace("copy", "").strip()
                folder = parts[1].strip()

                src = os.path.join(self.desktop, name)
                dest = os.path.join(self.desktop, folder)

                if os.path.exists(src) and os.path.exists(dest):
                    if os.path.isdir(src):
                        shutil.copytree(src, os.path.join(dest, name))
                    else:
                        shutil.copy2(src, dest)
                    return f"{name} copy ho gaya boss."
                else:
                    return "File ya folder nahi mila boss."
            except:
                return "Copy nahi ho paya boss."

        # ===== SEARCH =====
        if "search" in cmd or "find" in cmd:
            name = cmd.replace("search", "").replace("find", "").replace("file", "").replace("folder", "").strip()

            for root, dirs, files in os.walk(self.desktop):
                if name in files or name in dirs:
                    return f"Mil gaya boss: {os.path.join(root, name)}"

            return "Nahi mila boss."

        return None