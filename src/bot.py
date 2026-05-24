import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from config import CHANNEL_ID
from generate import generate
from post import send, format_message, get_channel_id

def main():
    print("📖 وكيل حكايات وعبر يعمل...")

    cid = CHANNEL_ID
    if cid and not cid.startswith("@"):
        found = get_channel_id()
        if found:
            cid = found
            print(f"📢 تم العثور على القناة: {cid}")
        else:
            print("⚠️ لم يتم العثور على القناة من getUpdates، استخدم CHANNEL_ID الموجود")
    else:
        print(f"📢 القناة: {cid}")

    print("✍️ جاري كتابة القصة...")
    content = generate()
    print("✅ تم إنشاء القصة")
    print("📝 النص الخام:", content[:200])

    msg = format_message(content)
    print("📤 جاري النشر... طول الرسالة:", len(msg), "حرف")

    result = send(cid, msg)
    if result.get("ok"):
        print("✅ تم النشر بنجاح!")
    else:
        print(f"❌ فشل النشر: {result.get('description', 'خطأ غير معروف')}")

if __name__ == "__main__":
    main()
