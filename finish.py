import requests

TOKEN = '8147028365:AAEiXp3FlWPCX8FsSzN3ZhqY2PGojUE_dbM'
CHAT_ID = '1069045255'
MESSAGE = """🌟 Поздравляю вас с завершением курса приёма лекарств!
Теперь я больше не буду напоминать вам о приёме таблеток.
Пусть болезни обходят вас стороной, а здоровье всегда будет крепким! 💊✨

Кстати, мой хозяин очень вас любит ❤️"""

requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage", params={"chat_id": CHAT_ID, "text": MESSAGE})
