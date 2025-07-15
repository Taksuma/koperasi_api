# File: users/views.py (KODE PERBAIKAN)

from rest_framework import viewsets
from .models import User
# Impor serializer yang sudah diperbaiki
from .serializers import UserRegistrationSerializer 

class UserViewSet(viewsets.ModelViewSet):
    """
    Endpoint untuk registrasi pengguna baru. Hanya mendukung method POST (create).
    """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    # Batasi agar endpoint ini hanya bisa untuk membuat user (POST)
    http_method_names = ['post']