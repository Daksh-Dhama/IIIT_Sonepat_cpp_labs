import os
import time
import requests
from bs4 import BeautifulSoup

# ==================== CONFIGURATION ====================
TOKEN = "8839708179:AAElGDecNHq8PCWawQWHLbITXFfy0HyL0cw"
CHAT_ID = "8970171497"
URL = "https://www.iiitsonepat.ac.in/"
CHECK_INTERVAL = 60  
# =======================================================

def trigger_alerts(alert_text, play_siren=False):
    """Sends a Telegram ping and optionally forces Windows to sound a loud alarm sequence."""
    # 1. Send Telegram Message
    telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": alert_text}
    try:
        requests.post(telegram_url, json=payload, timeout=15)
        print("🚀 Notification beamed to Telegram API pipeline.")
    except Exception as e:
        print(f"❌ Telegram failed: {e}")

    # 2. Trigger Laptop Siren (Only runs on an actual website change)
    if play_siren:
        print("🚨 INITIATING WINDOWS EMERGENCY ALARM PIPELINE! 🚨")
        try:
            for _ in range(12):
                os.system("powershell.exe -Command \"[Console]::Beep(850, 350)\"")
                time.sleep(0.1)
        except Exception as e:
            print(f"⚠️ Could not trigger local audio: {e}")

def get_website_hash():
    """Grabs the text content of the website to monitor changes."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    try:
        response = requests.get(URL, headers=headers, timeout=15)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup.get_text()
        return None
    except Exception:
        return None

def main():
    print("🛰️ Sentinel Activated. Pulling baseline layout snapshot...")
    last_state = get_website_hash()
    
    if not last_state:
        print("❌ Website structure unreachable. Retrying in 10 seconds...")
        time.sleep(10)
        return main()
        
    print("✅ Baseline snapshot locked. Active monitoring started.")
    # Notice play_siren=False here so it starts up silently
    trigger_alerts("🤖 Hostel Sentinel is officially online! System fully armed.", play_siren=False)

    while True:
        time.sleep(CHECK_INTERVAL)
        current_state = get_website_hash()
        
        if current_state is None:
            continue
            
        if current_state != last_state:
            print("🚨 PORTAL MODIFICATION DETECTED!")
            alert_msg = f"🚨 ALERT: PORTAL MODIFICATION DETECTED!\n\nCheck the IIIT Sonepat site immediately: {URL}"
            # Notice play_siren=True here so it wakes you up when the site actually updates!
            trigger_alerts(alert_msg, play_siren=True)
            last_state = current_state

if __name__ == "__main__":
    main()