# File: users/serializers.py (KODE PERBAIKAN)

from rest_framework import serializers
from django.db import transaction
from .models import User
from members.models import Member # Impor model Member

class UserRegistrationSerializer(serializers.ModelSerializer):
    # Field yang dibutuhkan dari Flutter, tidak disimpan di model User
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    name = serializers.CharField(write_only=True)
    address = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'name', 'address', 'phone_number']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password tidak cocok."})
        # Validasi tambahan: pastikan nomor telepon unik
        if Member.objects.filter(phone_number=attrs['phone_number']).exists():
            raise serializers.ValidationError({"phone_number": "Nomor telepon ini sudah terdaftar."})
        return attrs

    @transaction.atomic
    def create(self, validated_data):
        # 1. Buat User untuk login
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        # 2. Buat Member yang terhubung dengan User di atas
        Member.objects.create(
            user=user,
            name=validated_data['name'],
            address=validated_data['address'],
            phone_number=validated_data['phone_number']
        )
        return user