import json
import urllib.request

from config import GROQ_URL, GROQ_KEY

def generate():
    prompt = """أنت كاتب قصص وحكم. اكتب قصة قصيرة بالعربية الفصحى فيها عبرة وحكمة.

المطلوب:
1. عنوان جذاب للقصة
2. قصة قصيرة (200-400 كلمة) فيها حدث أو موقف
3. حكمة أو عبرة في نهاية القصة

أجب بالتنسيق التالي فقط:
العنوان: ...
القصة: ...
الحكمة: ...

تأكد أن القصة أصلية ومؤثرة."""
    body = json.dumps({
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": "أنت كاتب قصص عربي محترف. تكتب قصصاً قصيرة مؤثرة بالعربية الفصحى. كل قصة تحمل حكمة أو عبرة."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.8,
    }).encode()
    req = urllib.request.Request(GROQ_URL, data=body, headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_KEY}",
    })
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read())
    return data["choices"][0]["message"]["content"]
