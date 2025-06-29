# File: loans/serializers.py
from rest_framework import serializers
from .models import Loan, LoanPayment

class LoanSerializer(serializers.ModelSerializer):
    """
    Serializer untuk model Pinjaman (Loan).
    """
    class Meta:
        model = Loan
        fields = '__all__'
        read_only_fields = ['start_date', 'end_date'] # Field ini akan diisi otomatis

class LoanPaymentSerializer(serializers.ModelSerializer):
    """
    Serializer untuk model Pembayaran Pinjaman (LoanPayment).
    """
    class Meta:
        model = LoanPayment
        fields = '__all__'
        read_only_fields = ['payment_date'] # Field ini akan diisi otomatis