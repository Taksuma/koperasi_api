# users/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

# Buat router dan daftarkan ViewSet kita
router = DefaultRouter()
router.register(r'users', UserViewSet)

# URL patterns akan dibuat otomatis oleh router
urlpatterns = [
    path('', include(router.urls)),
]