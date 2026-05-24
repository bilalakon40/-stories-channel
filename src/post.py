import json
import urllib.request
import urllib.parse

from config import API_URL

def send(chat_id, text):
    data = urllib.parse.urlencode({
        "chat_id": chat_id,
        "text": text,
    }).encode()
    req = urllib.request.Request(f"{API_URL}/sendMessage", data=data)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())

def format_message(content):
    lines = content.strip().split("\n")
    title = ""
    story = ""
    wisdom = ""
    section = ""
    for line in lines:
        if line.startswith("العنوان:"):
            title = line.replace("العنوان:", "").strip()
            section = ""
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

    msg = f"""📖 {title}

{story}

💡 الحكمة:
{wisdom}

—-
حكايات وعبر 📚"""
    return msg
