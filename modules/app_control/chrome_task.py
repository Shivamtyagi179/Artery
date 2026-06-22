import webbrowser
import pyautogui
import time


class ChromeTask:
    def __init__(self):
        print("[ChromeTask] Advanced Ready")
        self.last_query = None

        self.sites = {
          
            "google": "https://www.google.com",
            "instagram": "https://www.instagram.com",
            "facebook": "https://www.facebook.com",
            "twitter": "https://twitter.com",
            "github": "https://github.com",
            "chatgpt": "https://chat.openai.com",
            "linkedin": "https://www.linkedin.com",
            "netflix": "https://www.netflix.com",
            "amazon": "https://www.amazon.com",
            "flipkart": "https://www.flipkart.com",
            "Calculator": "https://www.online-calculator.com",
}

    # ================= MAIN =================
    def open(self, query: str):
        query = query.lower().strip()
        self.last_query = query

        # 🎯 direct site
        if query in self.sites:
            webbrowser.open(self.sites[query])
            return f"{query} open kar diya boss."

        # 🌐 looks like URL
        if "." in query:
            if not query.startswith("http"):
                query = "https://" + query
            webbrowser.open(query)
            return f"{query} open kar diya boss."

        # 🔎 smart search
        search = query.replace(" ", "+")
        url = f"https://www.google.com/search?q={search}"
        webbrowser.open(url)

        return f"{query} search kar diya boss."

    # ================= CONTROLS =================
    def new_tab(self):
        pyautogui.hotkey("ctrl", "t")
        return "New tab open boss."

    def close_tab(self):
        pyautogui.hotkey("ctrl", "w")
        return "Tab close boss."

    def switch_tab(self):
        pyautogui.hotkey("ctrl", "tab")
        return "Tab switch boss."

    def back(self):
        pyautogui.hotkey("alt", "left")
        return "Peeche aa gaye boss."

    def forward(self):
        pyautogui.hotkey("alt", "right")
        return "Aage aa gaye boss."

    def refresh(self):
        pyautogui.press("f5")
        return "Page refresh boss."

    def scroll_down(self):
        pyautogui.scroll(-800)
        return "Scroll down boss."

    def scroll_up(self):
        pyautogui.scroll(800)
        return "Scroll up boss."

    # ================= SMART REUSE =================
    def search_again(self, new_query: str):
        pyautogui.hotkey("ctrl", "l")   # focus URL bar
        time.sleep(0.3)

        search = new_query.replace(" ", "+")
        url = f"https://www.google.com/search?q={search}"

        pyautogui.write(url)
        pyautogui.press("enter")

        return f"{new_query} dobara search kar diya boss."