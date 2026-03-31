# modules/app_control/whatsapp_task.py
import pyautogui
import time
import os

class WhatsAppDesktopEngine:
    def __init__(self):
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.5
    
    def open_whatsapp(self):
        """WhatsApp kholo"""
        pyautogui.hotkey('win', 's')
        time.sleep(0.5)
        pyautogui.write('whatsapp')
        pyautogui.press('enter')
        time.sleep(4)  # Full load wait
        print("[WhatsApp] WhatsApp opened")
        return "WhatsApp khol diya boss!"
    
    def send_message(self, contact, message):
        """1. Search → 2. Contact select → 3. Type → 4. Send"""
        try:
            print(f"[WhatsApp] Starting: {contact} <- '{message}'")
            
            # Step 1: WhatsApp open
            self.open_whatsapp()
            time.sleep(0.5)
            
            # Step 2: Search bar click (your coordinates)
            pyautogui.click(220, 128)  # Search bar center (85+365/2, 135+45/2)
            time.sleep(0.5)
            print("[WhatsApp] Search bar clicked")
            
            # Step 3: CLEAR search bar + type contact name
            pyautogui.hotkey('ctrl', 'a')  # Select all
            time.sleep(0.5)
            pyautogui.write(contact)  # "nikita" type
            print(f"[WhatsApp] Searched: {contact}")
            time.sleep(0.5)  # Search results load
            
            # Step 4: Click FIRST search result (contact)
            pyautogui.click(250, 320)  # First contact result area
            time.sleep(0.5)
            print("[WhatsApp] Contact selected")
            
            # Step 5: Message box click + type
            pyautogui.click(1170, 980)  # Message box center (195+485/2, 825+55/2)
            time.sleep(1)
            pyautogui.write(message)  # "hi" type
            print(f"[WhatsApp] Message typed: {message}")
            time.sleep(0.5)
            
            # Step 6: SEND
            pyautogui.press('enter')
            time.sleep(1)
            
            return f"✅ Boss, '{message}' successful send To '{contact}'...."
            
        except Exception as e:
            return f"Boss, error: {str(e)[:50]}"
    
    def check_messages(self):
        self.open_whatsapp()
        time.sleep(2)
        return "Haan boss, messages check kar liye!"
     
    def close_whatsapp(self):
        pyautogui.hotkey('alt', 'f4')
        time.sleep(0.5)
        return "WhatsApp band kar diya boss!"
    

