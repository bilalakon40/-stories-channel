import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
GROQ_KEY = os.environ.get("GROQ_API_KEY")
CHANNEL_ID = os.environ.get("CHANNEL_ID", "@حكايات_وعبر")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN غير موجود")
if not GROQ_KEY:
    raise ValueError("GROQ_API_KEY غير موجود")

API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
