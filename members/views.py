# members/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Member
from .serializers import MemberSerializer
from loans.serializers import LoanSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all().order_by('name')
    serializer_class = MemberSerializer

    @action(detail=True, methods=['get'])
    def loans(self, request, pk=None):
        """
        Mengambil semua pinjaman untuk anggota tertentu.
        """
        member = self.get_object()
        loans = member.loans.all()
        serializer = LoanSerializer(loans, many=True, context={'request': request})
        return Response(serializer.data)