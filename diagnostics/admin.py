from django.contrib import admin
from .models import Patient, MedicalImage
from .ai_model import predict_chihuahua_or_muffin

@admin.action(description="Run AI Diagnostics")
def run_ai_diagnostics(modeladmin, request, queryset):
    success_count = 0
    # วนลูปตามรูปที่ถูกติ๊กเลือก
    for instance in queryset:
        # ป้องกัน Error กรณีรูปถูกลบไฟล์ทิ้งไปแล้ว
        if instance.image_file:
            # โยนรูปเก่าไปให้ AI คิดใหม่
            ai_decision = predict_chihuahua_or_muffin(instance.image_file.path)
            # บันทึกผลลัพธ์
            instance.ai_result = ai_decision
            instance.save()
            success_count += 1
    modeladmin.message_user(request, f"Completed {success_count} AI diagnostic(s)")

@admin.action(description="Reset prediction to PENDING")
def reset_to_pending(modeladmin, request, queryset):
    # เปลี่ยนสถานะรูปทั้งหมดที่ติ๊กเลือก ให้กลับเป็น PENDING ทันที (ไม่ต้องวนลูป)
    queryset.update(ai_result='PENDING')
    modeladmin.message_user(request, "Reset prediction_result Done")

class MedicalImageAdmin(admin.ModelAdmin):
    actions = [run_ai_diagnostics, reset_to_pending]

admin.site.register(Patient)
admin.site.register(MedicalImage, MedicalImageAdmin)