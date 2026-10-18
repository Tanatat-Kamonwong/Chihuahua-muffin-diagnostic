from django.contrib import admin
from .models import Patient, MedicalImage

admin.site.register(Patient)
admin.site.register(MedicalImage)

# Register your models here.
