import json
import urllib.request
import urllib.parse

from config import API_URL

def send(chat_id, text):
    data = urllib.parse.urlencode({
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
    }).encode()
    req = urllib.request.Request(f"{API_URL}/sendMessage", data=data)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())

def get_channel_id():
    data = urllib.parse.urlencode({"timeout": 5}).encode()
    req = urllib.request.Request(f"{API_URL}/getUpdates", data=data)
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read())
    if result.get("ok") and result["result"]:
        for update in result["result"]:
            msg = update.get("message") or update.get("channel_post", {})
            chat = msg.get("chat", {})
            if chat.get("type") in ("channel", "supergroup") and chat.get("id"):
                return chat["id"]
    return None

def format_message(content):
    lines = content.strip().split("\n")
    title = ""
    story = ""
    wisdom = ""
    section = ""
    for line in lines:
        if line.startswith("العنوان:"):
            title = line.replace("العنوان:", "").strip()
            section = "title"
        elif line.startswith("القصة:"):
            section = "story"
        elif line.startswith("الحكمة:"):
            section = "wisdom"
        elif section == "story":
            story += line + "\n"
        elif section == "wisdom":
            wisdom += line + "\n"

    title = title or "قصة وعبرة"
    story = story.strip()
    wisdom = wisdom.strip() or "في كل قصة عبرة"

    msg = f"""📖 <b>{title}</b>

{story}

💡 <b>الحكمة:</b>
{wisdom}

—-
<b>حكايات وعبر</b> 📚"""
    return msg
