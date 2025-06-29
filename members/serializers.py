# File: members/serializers.py
from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    """
    Serializer untuk model Anggota (Member).
    Mengubah objek Member menjadi JSON dan sebaliknya.
    """
    class Meta:
        model = Member
        fields = '__all__' # Menggunakan semua field dari model
        read_only_fields = ['date_joined'] # Field ini hanya bisa dibaca, tidak bisa diubah saat POST/PUT