import os
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
r = requests.get(ZARA_URL, headers=headers, timeout=20)
soup = BeautifulSoup(r.text, "html.parser")
text = soup.get_text().upper()

if TAGLIA in text and "NON DISPONIBILE" not in text:
    send(f"🔥 TAGLIA {TAGLIA} DISPONIBILE!\n{ZARA_URL}")
