# File: deposits/serializers.py
from rest_framework import serializers
from .models import Deposit

class DepositSerializer(serializers.ModelSerializer):
    """
    Serializer untuk model Simpanan (Deposit).
    """
    class Meta:
        model = Deposit
        fields = '__all__'
        read_only_fields = ['deposit_date']