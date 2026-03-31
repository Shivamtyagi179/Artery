# core/intent_router.py - PURE ROUTER (NO FIXED DATA!)
from typing import Dict, Any

class IntentRouter:
    def __init__(self):
        # Intent → Task Engine mapping (DYNAMIC!)
        self.task_engine_map = {
            # WHATSAPP
            "whatsapp_message": "task_engine.whatsapp_engine",
            "whatsapp_open": "task_engine.whatsapp_engine",
            
            # YOUTUBE  
            "youtube_play": "task_engine.system.control.youtube_task",
            "youtube_next": "task_engine.system.controlyoutube_task",
            "youtube_previous": "task_engine.youtube_task", 
            "youtube_fullscreen": "task_engine.youtube_task",
            
            # SYSTEM
            "volume_up": "task_engine.system_engine",
            "volume_down": "task_engine.system_engine",
            "mute": "task_engine.system_engine",
            "shutdown": "task_engine.system_engine",
            "restart": "task_engine.system_engine",
            
            # APPS
            "open_chrome": "task_engine.system.control",
            "open_edge": "task_engine.system.control", 
            "open_vscode": "task_engine.system.control",
            "open_notepad": "task_engine.system.control",
            "open_calculator": "task_engine.system.control"
        }
        print("🧠 IntentRouter Ready - 100% DYNAMIC!")

    def route(self, intent_data: Dict[str, Any]) -> Dict[str, Any]:
        """WHATEVER CommandParser dega - bilkul waisa forward!"""
        intent = intent_data.get("intent", "unknown")
        entities = intent_data.get("entities", {})  # Jo bhi mile!
        confidence = intent_data.get("confidence", 0.0)
        
        print(f"🧠 ROUTING: '{intent}'")
        print(f"📋 ENTITIES (AS-IS): {entities}")  # Exact copy!
        
        # Task Engine find karo
        task_engine = self.task_engine_map.get(intent)
        if task_engine:
            print(f"✅ ROUTED → {task_engine}")
            return {
                "routed_to": task_engine,
                "intent": intent,
                "entities": entities,  # 100% CommandParser se copy!
                "confidence": confidence,
                "status": "routed"
            }
        
        print("❌ UNKNOWN INTENT")
        return {
            "routed_to": None,
            "intent": intent,
            "entities": intent_data.get("entities", {}),  # Jo bhi mile!
            "confidence": confidence,
            "status": "unknown"
        }

# ========== NO TEST DATA! ==========
if __name__ == "__main__":
    print("IntentRouter ready - waiting for CommandParser data!")
