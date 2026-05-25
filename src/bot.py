import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from config import CHANNEL_ID
from generate import generate
from post import send

def main():
    print("📖 وكيل حكايات وعبر يعمل...")

    cid = CHANNEL_ID
    print(f"📢 القناة: {cid}")

    print("✍️ جاري كتابة القصة...")
    content = generate()
    print("✅ تم إنشاء القصة")
    print(f"📝 طول النص الخام: {len(content)} حرف")
    print("📝 أول 100 حرف:", content[:100])

    msg = content.strip()
    print(f"📤 جاري النشر... طول الرسالة: {len(msg)} حرف")

    result = send(cid, msg)
    if result.get("ok"):
        print("✅ تم النشر بنجاح!")
    else:
        print(f"❌ فشل النشر: {result.get('description', 'خطأ غير معروف')}")

if __name__ == "__main__":
    main()
