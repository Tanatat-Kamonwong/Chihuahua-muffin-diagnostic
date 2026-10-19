from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, MedicalImageViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'images', MedicalImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]