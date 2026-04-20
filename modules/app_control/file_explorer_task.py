import os
import shutil
import subprocess

class FileExplorerTask:
    def __init__(self):
        self.desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        self.downloads = os.path.join(os.path.expanduser("~"), "Downloads")

        self.last_folder = None
        self.last_file = None

    # ================= MAIN =================
    def handle(self, cmd: str):
        cmd = cmd.lower().strip()

        # ===== CREATE FOLDER =====
        if "create folder" in cmd or "folder bana" in cmd:
            name = cmd.split()[-1]
            path = os.path.join(self.desktop, name)

            os.makedirs(path, exist_ok=True)
            self.last_folder = path

            return f"Folder '{name}' desktop par bana diya boss."

        # ===== CREATE FILE =====
        if "create file" in cmd or "file bana" in cmd:
            name = cmd.split()[-1]

            if "." not in name:
                name += ".txt"

            folder = self.last_folder if self.last_folder else self.desktop
            path = os.path.join(folder, name)

            with open(path, "w") as f:
                f.write("")

            self.last_file = path
            return f"File '{name}' create ho gayi boss."

        # ===== DELETE =====
        if "delete file" in cmd:
            name = cmd.split()[-1]
            path = os.path.join(self.desktop, name)

            if os.path.exists(path):
                os.remove(path)
                return f"{name} delete ho gaya boss."
            return "File nahi mili boss."

        if "delete folder" in cmd:
            name = cmd.split()[-1]
            path = os.path.join(self.desktop, name)

            if os.path.exists(path):
                shutil.rmtree(path)
                return f"{name} folder delete ho gaya boss."
            return "Folder nahi mila boss."

        # ===== OPEN =====
        if "open file" in cmd:
            name = cmd.split()[-1]
            path = os.path.join(self.desktop, name)

            if os.path.exists(path):
                os.startfile(path)
                self.last_file = path
                return f"{name} open kar diya boss."
            return "File nahi mili boss."

        if "open folder" in cmd:
            name = cmd.split()[-1]
            path = os.path.join(self.desktop, name)

            if os.path.exists(path):
                os.startfile(path)
                self.last_folder = path
                return f"{name} folder open kar diya boss."
            return "Folder nahi mila boss."

        if "open last file" in cmd and self.last_file:
            os.startfile(self.last_file)
            return "Last file open kar diya boss."

        # ===== LIST FILES =====
        if "list files" in cmd or "show files" in cmd:
            folder = self.last_folder if self.last_folder else self.desktop

            try:
                files = os.listdir(folder)
                return "Files:\n" + "\n".join(files[:20])
            except:
                return "Folder access nahi ho pa raha boss."

        # ===== RENAME =====
        if "rename file" in cmd:
            parts = cmd.split()
            old = parts[-2]
            new = parts[-1]

            old_path = os.path.join(self.desktop, old)
            new_path = os.path.join(self.desktop, new)

            if os.path.exists(old_path):
                os.rename(old_path, new_path)
                return f"{old} rename karke {new} kar diya boss."
            return "File nahi mili boss."

        # ===== MOVE =====
        if "move file" in cmd:
            parts = cmd.split()
            file_name = parts[2]
            folder_name = parts[-1]

            src = os.path.join(self.desktop, file_name)
            dest_folder = os.path.join(self.desktop, folder_name)

            if os.path.exists(src) and os.path.exists(dest_folder):
                shutil.move(src, dest_folder)
                return f"{file_name} move kar diya {folder_name} me."
            return "File ya folder nahi mila boss."

        # ===== COPY =====
        if "copy file" in cmd:
            parts = cmd.split()
            file_name = parts[2]
            folder_name = parts[-1]

            src = os.path.join(self.desktop, file_name)
            dest_folder = os.path.join(self.desktop, folder_name)

            if os.path.exists(src) and os.path.exists(dest_folder):
                shutil.copy(src, dest_folder)
                return f"{file_name} copy ho gaya {folder_name} me."
            return "File ya folder nahi mila boss."

        # ===== SEARCH =====
        if "find file" in cmd or "search file" in cmd:
            name = cmd.split()[-1]

            for root, dirs, files in os.walk(self.desktop):
                if name in files:
                    path = os.path.join(root, name)
                    return f"File mili boss: {path}"

            return "File nahi mili boss."

        return None