import requests

TOKEN = '8147028365:AAEiXp3FlWPCX8FsSzN3ZhqY2PGojUE_dbM'
CHAT_ID = '1069045255'
MESSAGE = """🕗 Утренний приём (08:00):
- Ганатон
- Магне В6
- Мотинорм
- Melatonin 3mg
- Витамин D3"""

requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage", params={"chat_id": CHAT_ID, "text": MESSAGE})
