import os
import shutil

def create_file(name):
    try:
        open(name, "w").close()
        return f"{name} file bana di boss."
    except:
        return "File create nahi ho paayi boss."

def create_folder(name):
    try:
        os.makedirs(name, exist_ok=True)
        return f"{name} folder bana diya boss."
    except:
        return "Folder create nahi ho paaya boss."

def delete_item(name):
    try:
        if os.path.isfile(name):
            os.remove(name)
        elif os.path.isdir(name):
            shutil.rmtree(name)
        else:
            return "File ya folder mila nahi boss."
        return f"{name} delete kar diya boss."
    except:
        return "Delete nahi ho paaya boss."

def list_files(path="."):
    try:
        files = os.listdir(path)
        return "Files:\n" + "\n".join(files[:10])
    except:
        return "Files read nahi ho paaye boss."