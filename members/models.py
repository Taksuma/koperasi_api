# File: members/models.py (KODE PERBAIKAN)

from django.db import models
from users.models import User # <-- PENTING: Impor model User kustom Anda

class Member(models.Model):
    # PERBAIKAN: Menambahkan hubungan 'satu-ke-satu' ke model User.
    # Ini menjadikan User sebagai "kunci utama" dari Member.
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    # Field lainnya tetap sama
    name = models.CharField(max_length=255, verbose_name="Nama Anggota")
    address = models.TextField(verbose_name="Alamat")
    phone_number = models.CharField(max_length=20, verbose_name="Nomor Telepon", unique=True)
    date_joined = models.DateField(auto_now_add=True, verbose_name="Tanggal Bergabung")

    def __str__(self):
        # Tampilkan username dari User yang terhubung untuk kejelasan
        return self.user.username

    class Meta:
        verbose_name = "Anggota"
        verbose_name_plural = "Anggota"
        ordering = ['name']