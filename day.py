import requests

TOKEN = '8147028365:AAEiXp3FlWPCX8FsSzN3ZhqY2PGojUE_dbM'
CHAT_ID = '1069045255'
MESSAGE = """🕜 Дневной приём (13:30):
- Ганатон
- Дюспаталин
- Улсепан
- Фолиевая кислота (сосательные)"""

requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage", params={"chat_id": CHAT_ID, "text": MESSAGE})
