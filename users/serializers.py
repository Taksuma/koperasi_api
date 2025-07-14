# users/serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    # Field konfirmasi password, tidak akan disimpan di database (write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        # Field yang akan diproses saat registrasi
        fields = ['username', 'password', 'password2']
        extra_kwargs = {
            # Pastikan password tidak pernah dikirim kembali ke client
            'password': {'write_only': True}
        }

    # Fungsi ini dipanggil untuk validasi data
    def validate(self, attrs):
        # Cek apakah password dan konfirmasi password sama
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password tidak cocok."})
        return attrs

    # Fungsi ini dipanggil saat user baru dibuat
    def create(self, validated_data):
        # Gunakan create_user untuk memastikan password di-hash (enkripsi)
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user