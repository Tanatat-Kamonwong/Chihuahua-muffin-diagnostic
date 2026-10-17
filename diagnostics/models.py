from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    #Table 1
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class MedicalImage(models.Model):
    #Table 2
    RESULT_CHOICES = (
        ('PENDING', 'Pending'),
        ('CHIHUAHUA', 'Chihuahua'),
        ('MUFFIN', 'Blueberry Muffin'),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='images')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image_file = models.ImageField(upload_to='medical_images/')
    ai_result = models.CharField(max_length=20, choices=RESULT_CHOICES, default='PENDING')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image ID:{self.id} - {self.patient.first_name} [{self.ai_result}]"
