# loans/serializers.py
from rest_framework import serializers
from .models import Loan, LoanPayment

class LoanSerializer(serializers.ModelSerializer):
    member_name = serializers.StringRelatedField(source='member.name', read_only=True)
    class Meta:
        model = Loan
        fields = ['id', 'member', 'member_name', 'amount', 'interest_rate', 'term_months', 'start_date', 'end_date', 'status']

class LoanPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanPayment
        fields = '__all__'