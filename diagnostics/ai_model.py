# ไฟล์: diagnostics/ai_model.py
from PIL import Image
from transformers import pipeline
import warnings

# ปิดการแจ้งเตือนจุกจิกของ Hugging Face
warnings.filterwarnings("ignore")

print("กำลังโหลดสมอง AI เข้าสู่ระบบ (อาจใช้เวลาสักครู่ในครั้งแรก)...")
# โหลดโมเดล ViT มาไว้ใน RAM ของเครื่อง (ใช้ Pipeline สำเร็จรูป)
classifier = pipeline("image-classification", model="google/vit-base-patch16-224")
print("โหลด AI สำเร็จ! ระบบพร้อมวิเคราะห์แล้ว")

def predict_chihuahua_or_muffin(image_path):
    """
    ฟังก์ชันอ่านไฟล์รูปภาพ และวิเคราะห์ผลด้วย CPU ของเครื่องเราเอง
    """
    try:
        print(f"\n[Debug 1] AI กำลังเปิดไฟล์: {image_path}")
        # 1. เปิดไฟล์ภาพด้วยไลบรารี Pillow
        image = Image.open(image_path)
        
        # 2. ให้โมเดล AI ในเครื่องทำนายผล 
        # (มันจะคืนค่ากลับมาเหมือนที่ API เคยทำเป๊ะๆ เช่น [{'label': 'Chihuahua', 'score': 0.95}, ...])
        predictions = classifier(image)

        print(f"[Debug 2] AI ทายว่า: {predictions}")
        
        # 3. แปลงคำตอบให้ตรงกับฐานข้อมูลของเรา
        for pred in predictions:
            label = pred.get('label', '').lower()
            
            # ถ้า AI มั่นใจว่าเป็นชิวาว่า หรือหมา
            if 'chihuahua' in label or 'dog' in label:
                return 'CHIHUAHUA'
            # ถ้า AI มั่นใจว่าเป็นมัฟฟิน คัพเค้ก หรือเบเกอรี่
            elif 'muffin' in label or 'cupcake' in label or 'bakery' in label:
                return 'MUFFIN'

        print("[Debug 3] ไม่เข้าเงื่อนไขเลย ระบบจึงตั้งค่าเป็น PENDING")
        # ถ้าหาไม่เจอทั้งสองอย่าง
        return 'PENDING'
        
    except Exception as e:
        print(f"Local AI Error: {e}")
        return 'PENDING'