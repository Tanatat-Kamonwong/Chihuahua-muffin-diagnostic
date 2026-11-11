from rest_framework import viewsets
from .models import Patient, MedicalImage
from .serializers import PatientSerializer, MedicalImageSerializer
from .ai_model import predict_chihuahua_or_muffin

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class MedicalImageViewSet(viewsets.ModelViewSet):
    queryset = MedicalImage.objects.all()
    serializer_class = MedicalImageSerializer

    def perform_create(self, serializer):
        # 2.1 บันทึกข้อมูลและรูปภาพลงฮาร์ดดิสก์ก่อน เพื่อให้เกิดไฟล์จริงๆ
        image_instance = serializer.save(uploaded_by=self.request.user)

        # 2.2 ส่งที่อยู่ไฟล์ภาพ (Path) ไปให้ AI วิเคราะห์ 
        # (ใช้ .image_file.path ให้ตรงกับชื่อตัวแปรในโมเดลของคุณ)
        ai_decision = predict_chihuahua_or_muffin(image_instance.image_file.path)

        # 2.3 นำผลลัพธ์ ('CHIHUAHUA', 'MUFFIN' หรือ 'PENDING') ไปใส่ในฟิลด์ ai_result
        image_instance.ai_result = ai_decision
        
        # 2.4 สั่งบันทึกข้อมูลลงฐานข้อมูลอีกครั้งเพื่ออัปเดตผลลัพธ์
        image_instance.save()