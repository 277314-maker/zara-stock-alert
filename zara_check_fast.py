import os
import time
import requests
from bs4 import BeautifulSoup

ZARA_URL = "https://www.zara.com/it/it/body-in-pizzo-p06050805.html"
TAGLIA = "S"

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def send(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

headers = {"User-Agent": "Mozilla/5.0"}
print("Monitor veloce attivo")

for _ in range(30):  # ~60 minuti
    try:
        r = requests.get(ZARA_URL, headers=headers, timeout=20)
        text = BeautifulSoup(r.text, "html.parser").get_text().upper()

        if TAGLIA in text and "NON DISPONIBILE" not in text:
            send(f"🔥 TAGLIA {TAGLIA} DISPONIBILE!\n{ZARA_URL}")
            break
        else:
            print("Ancora non disponibile")

    except Exception as e:
        print("Errore:", e)

    time.sleep(120)
