import requests

from config import GROQ_URL, GROQ_KEY

def generate():
    body = {
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
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_KEY}",
    }
    resp = requests.post(GROQ_URL, json=body, headers=headers, timeout=60)
    if resp.status_code != 200:
        raise Exception(f"Groq API error {resp.status_code}: {resp.text[:300]}")
    data = resp.json()
    return data["choices"][0]["message"]["content"]
