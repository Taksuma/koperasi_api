# File: loans/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Loan, LoanPayment
from .serializers import LoanSerializer, LoanPaymentSerializer

class LoanViewSet(viewsets.ModelViewSet):
    """
    API endpoint yang memungkinkan Pinjaman untuk dilihat, dibuat, atau diperbarui.
    """
    queryset = Loan.objects.all().order_by('-start_date')
    serializer_class = LoanSerializer

    # Tambahan: Endpoint kustom untuk mengubah status pinjaman
    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        """Menyetujui pinjaman."""
        loan = self.get_object()
        loan.status = 'approved'
        # Kamu bisa menambahkan logika lain di sini,
        # misalnya menghitung tanggal jatuh tempo
        loan.save()
        serializer = self.get_serializer(loan)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        """Menolak pinjaman."""
        loan = self.get_object()
        loan.status = 'rejected'
        loan.save()
        serializer = self.get_serializer(loan)
        return Response(serializer.data)

class LoanPaymentViewSet(viewsets.ModelViewSet):
    """
    API endpoint yang memungkinkan Pembayaran Pinjaman untuk dilihat, dibuat, atau diedit.
    """
    queryset = LoanPayment.objects.all().order_by('-payment_date')
    serializer_class = LoanPaymentSerializer