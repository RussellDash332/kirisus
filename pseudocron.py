try:    TOKEN, CHAT, MSG = os.environ['TOKEN'], os.environ['CHAT'], os.environ['MSG']
except: from env import TOKEN, CHAT, MSG
import requests, emoji

print(requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage", params={
    "chat_id": CHAT,
    "parse_mode": "Markdown",
    "text": emoji.emojize(MSG),
    "disable_web_page_preview": True,
}).json())