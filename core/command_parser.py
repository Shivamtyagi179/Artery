# core/command_parser.py
import re
from typing import Dict, List, Optional

class CommandParser:
    def __init__(self):
        self.wake_words = ["artery", "arteri", "आर्टरी"]
        self.intents = {
            # ========== WHATSAPP ==========
            "whatsapp_message": {
                "triggers": ["message", "msg", "bhej", "message karo", "मैसेज", "भेजो"],
                "entities": ["contact", "message"]
            },
            "whatsapp_open": {
                "triggers": ["whatsapp", "whatshap", "व्हाट्सएप", "whatsapp kholo"],
                "entities": []
            },
            
            # ========== YOUTUBE ==========
            "youtube_play": {
                "triggers": ["play"],
                "entities": ["song"]
            },
            "youtube_next": {
                "triggers": ["next", "आगे"],
                "entities": []
            },
            "youtube_previous": {
                "triggers": ["previous", "पिछला", "back"],
                "entities": []
            },
            "youtube_fullscreen": {
                "triggers": ["fullscreen", "full screen"],
                "entities": []
            },
            
            # ========== APPS ==========
            "open_chrome": {"triggers": ["open chrome", "क्रोम खोलो"]},
            "open_edge": {"triggers": ["open edge"]},
            "open_vscode": {"triggers": ["open vscode", "open vs code", "कोड खोलो"]},
            "open_notepad": {"triggers": ["open notepad", "नोटपैड"]},
            "open_calculator": {"triggers": ["open calculator", "कैलकुलेटर"]},
            
            # ========== SYSTEM ==========
            "volume_up": {"triggers": ["volume up", "आवाज़ बढ़ाओ"]},
            "volume_down": {"triggers": ["volume down", "आवाज़ कम"]},
            "mute": {"triggers": ["mute", "म्यूट"]},
            "shutdown": {"triggers": ["shutdown", "बंद करो"]},
            "restart": {"triggers": ["restart", "रीस्टार्ट"]}
        }
        
        self.skip_words = {
            "ko", "karo", "kar", "do", "hai", "है", "का", "की", "के", "में", "से", 
            "को", "the", "a", "an", "is", "are", "ho", "जा", "रहा"
        }

    def parse(self, raw_command: str) -> Dict:
        """Raw voice → Structured intent"""
        cmd = raw_command.lower().strip()
        print(f"🔍 RAW: '{raw_command}' → '{cmd}'")
        
        # Wake word check
        if not any(wake in cmd for wake in self.wake_words):
            print("❌ Wake word missing")
            return {"intent": "unknown", "confidence": 0.0, "entities": {}}
        
        # Remove wake word
        clean_cmd = re.sub(r'\b(artery|arteri|आर्टरी)\b', '', cmd).strip()
        
        # Find intent
        intent_data = self._find_intent(clean_cmd)
        if intent_data["intent"] == "unknown":
            return intent_data
        
        # Extract entities
        entities = self._extract_entities(clean_cmd, intent_data["intent"])
        
        return {
            "intent": intent_data["intent"],
            "confidence": intent_data["confidence"],
            "entities": entities,
            "raw_command": raw_command
        }

    def _find_intent(self, cmd: str) -> Dict:
        """Match best intent"""
        best = {"intent": "unknown", "confidence": 0.0}
        
        for intent, config in self.intents.items():
            hits = sum(1 for trigger in config["triggers"] if trigger in cmd)
            if hits > 0:
                confidence = min(1.0, hits * 0.3 + 0.2)
                if confidence > best["confidence"]:
                    best = {"intent": intent, "confidence": confidence}
        
        return best

    def _extract_entities(self, cmd: str, intent: str) -> Dict:
        """Smart entity extraction"""
        words = [w for w in cmd.split() if w not in self.skip_words]
        entities = {}
        
        if "whatsapp_message" in intent:
            contact, msg = self._get_message_parts(words)
            entities["contact"] = contact or "unknown"
            entities["message"] = msg or "hi"
            
        elif "youtube_play" in intent:
            entities["song"] = " ".join(words[1:]) or "music"
            
        elif any(x in intent for x in ["open_chrome", "open_edge", "open_vscode"]):
            entities["app"] = intent.split("_")[1]
            
        return entities

    def _get_message_parts(self, words: List[str]) -> tuple:
        """Contact + Message extract"""
        contact = ""
        message = ""
        
        for i, word in enumerate(words):
            if len(word) > 2 and word not in self.skip_words:
                if not contact:
                    contact = word
                else:
                    message = " ".join(words[i:])
                    break
        return contact, message

# ========== TEST ==========
if __name__ == "__main__":
    parser = CommandParser()
    tests = [
        "Artery shivam ko hi message karo",
        "Artery whatsapp kholo",
        "Artery play shape of you",
        "Artery volume up",
        "Artery open chrome"
    ]
    
    for test in tests:
        print(f"\n🧪 {test}")
        result = parser.parse(test)
        print(f"✅ {result}")
