import json
import urllib.request
import urllib.error

from config import GROQ_URL, GROQ_KEY

def generate():
    body = json.dumps({
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": "أنت كاتب قصص عربي محترف. تكتب قصصاً قصيرة مؤثرة بالعربية الفصحى. كل قصة تحمل حكمة أو عبرة."},
            {"role": "user", "content": """اكتب قصة قصيرة بالعربية الفصحى فيها عبرة وحكمة.

المطلوب:
1. عنوان جذاب للقصة
2. قصة قصيرة (200-400 كلمة) فيها حدث أو موقف مؤثر
3. حكمة أو عبرة واضحة في النهاية

أجب بالتنسيق التالي فقط:
العنوان: ...
القصة: ...
الحكمة: ..."""}
        ],
        "temperature": 0.8,
        "max_tokens": 1000,
    })
    req = urllib.request.Request(
        GROQ_URL,
        data=body.encode(),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {GROQ_KEY}",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read())
        return data["choices"][0]["message"]["content"]
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        raise Exception(f"HTTP {e.code}: {error_body[:300]}")
