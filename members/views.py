# File: members/views.py
from rest_framework import viewsets
from .models import Member
from .serializers import MemberSerializer

class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint yang memungkinkan Anggota untuk dilihat atau diedit.
    """
    queryset = Member.objects.all().order_by('name')
    serializer_class = MemberSerializer