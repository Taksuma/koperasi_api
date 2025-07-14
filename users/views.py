# users/views.py
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint yang memungkinkan pengguna untuk dilihat atau diedit.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer