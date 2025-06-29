# File: deposits/views.py
from rest_framework import viewsets
from .models import Deposit
from .serializers import DepositSerializer

class DepositViewSet(viewsets.ModelViewSet):
    """
    API endpoint yang memungkinkan transaksi Simpanan untuk dilihat atau diedit.
    """
    queryset = Deposit.objects.all().order_by('-deposit_date')
    serializer_class = DepositSerializer