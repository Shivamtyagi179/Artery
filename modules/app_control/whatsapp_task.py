import pyautogui
import time


class WhatsAppDesktopEngine:
    def __init__(self):
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.5

    def open_whatsapp(self):
        pyautogui.hotkey('win', 's')
        time.sleep(0.5)

        pyautogui.write('whatsapp')
        time.sleep(0.5)

        pyautogui.press('enter')
        time.sleep(5)

        return "WhatsApp opened"

    def send_message(self, contact, message):
        try:
            print(f"[WhatsApp] {contact} <- {message}")

            self.open_whatsapp()

            # Search bar
            pyautogui.click(219, 128)
            time.sleep(1)

            # Clear
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('backspace')
            time.sleep(0.5)

            # Type contact
            pyautogui.write(contact, interval=0.05)
            time.sleep(2)

            # Select contact
            pyautogui.press('down')
            time.sleep(0.5)
            pyautogui.press('enter')
            time.sleep(1)

            # Message box
            pyautogui.click(1170, 980)
            time.sleep(0.5)

            # Type message
            pyautogui.write(message, interval=0.03)
            time.sleep(0.5)

            # Send
            pyautogui.press('enter')

            return f"Message sent to {contact}"

        except Exception as e:
            return f"Error: {str(e)}"

    def close_whatsapp(self):
        pyautogui.hotkey('alt', 'f4')
        return "WhatsApp closed"