from core.command_parser import CommandParser
from core.memory_manager import MemoryManager
from core.safe_internet import SafeInternet

#from core.conversation_engine import BasicConversation

from modules.system_control import SystemControl

class TaskEngine:
    def __init__(self):
        self.parser = CommandParser()
        self.memory = MemoryManager()
        self.internet = SafeInternet()

        self.system = SystemControl()

        # basic conversational fallback
        #self.conversation = BasicConversation()

        print("[TaskEngine] Initialized")

    # ================= MAIN ENTRY =================
    def execute_command(self, text: str):
        if not text:
            return None

        text = text.lower().strip()

        # save memory
        self.memory.remember(text)

        # wake word handling
        if text.startswith("artery"):
            text = text.replace("artery", "", 1).strip()

        if not text:
            return None

        # ================= SYSTEM CONTROL =================
        system_reply = self.system.handle(text)
        if system_reply:
            return system_reply

        # ================= BASIC CONVERSATION FALLBACK =================
       
      #  conv_reply = self.conversation.handle(text)
       # if conv_reply:
        #    return conv_reply

        return "Boss, I couldn't understand the command."