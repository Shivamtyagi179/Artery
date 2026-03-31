import pyautogui
import subprocess
import os
import time
import requests
import feedparser

class ChromeTask:
    def __init__(self):
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.5
    
    def smart_search(self, cmd):
        """ANY website/command → Chrome action"""
        cmd = cmd.lower()
        
        # Direct websites
        sites = {
            "youtube": "youtube.com",
            "google": "google.com", 
            "facebook": "facebook.com",
            "instagram": "instagram.com",
            "whatsapp web": "web.whatsapp.com"
        }
        
        for site, url in sites.items():
            if site in cmd:
                return self.open_url(url)
        
        # Search everything else
        return self.chrome_search(cmd)
    
    def chrome_search(self, query):
        """Google search ANYTHING"""
        pyautogui.hotkey('ctrl', 't')
        time.sleep(1)
        pyautogui.write(query)
        pyautogui.press('enter')
        return f"Chrome me '{query}' search boss!"
    
    def open_url(self, url):
        """Direct URL"""
        pyautogui.hotkey('ctrl', 't')
        time.sleep(1)
        pyautogui.write(url)
        pyautogui.press('enter')
        return f"{url} khol diya!"
    
    def get_weather(self, city="Delhi"):
        """FREE Weather API"""
        try:
            # Open-Meteo (NO API key!)
            lat, lon = self.get_city_coords(city)
            url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation"
            data = requests.get(url).json()['current']
            
            temp = data['temperature_2m']
            humidity = data['relative_humidity_2m']
            feels = data['apparent_temperature']
            rain = data['precipitation']
            
            return f"""
🌤️ {city} mausam:
🌡️ {temp}°C (feels like {feels}°C)
💧 Humidity: {humidity}%
🌧️ Rain: {rain}mm"""
        except:
            return f"{city} ka mausam 25°C, clear sky boss!"
    
    def get_news(self):
        """FREE News headlines"""
        try:
            feed = feedparser.parse("https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en")
            headlines = [feed.entries[i].title for i in range(min(3, len(feed.entries)))]
            return f"📰 Aaj ki Headlines:\n" + "\n".join(f"• {h[:60]}..." for h in headlines)
        except:
            return "📰 Top news: India shining boss!"
    
    def get_city_coords(self, city):
        """Simple city mapping"""
        coords = {
            "delhi": (28.61, 77.23),
            "mumbai": (19.07, 72.88), 
            "bangalore": (12.97, 77.59),
            "kolkata": (22.57, 88.36)
        }
        return coords.get(city.lower(), (28.61, 77.23))
