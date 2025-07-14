# deposits/serializers.py
from rest_framework import serializers
from .models import Deposit

class DepositSerializer(serializers.ModelSerializer):
    # Tampilkan nama anggota, bukan hanya ID. `read_only=True` berarti
    # field ini tidak perlu diisi saat membuat simpanan baru.
    member_name = serializers.StringRelatedField(source='member.name', read_only=True)

    class Meta:
        model = Deposit
        # 'member' untuk membuat/update, 'member_name' untuk membaca
        fields = ['id', 'member', 'member_name', 'amount', 'deposit_date', 'description']