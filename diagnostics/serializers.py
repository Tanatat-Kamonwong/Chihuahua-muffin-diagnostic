from rest_framework import serializers
from .models import Patient, MedicalImage

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class MedicalImageSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.__str__', read_only=True)
    
    class Meta:
        model = MedicalImage
        fields = ['id', 'patient', 'patient_name', 'uploaded_by', 'image_file', 'ai_result', 'uploaded_at']
        read_only_fields = ['ai_result', 'uploaded_by']