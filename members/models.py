from django.db import models
from django.db import models
from users.models import User  # Impor model User kustom

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member')
    name = models.CharField(max_length=255, verbose_name="Nama Anggota")
    address = models.TextField(verbose_name="Alamat")
    phone_number = models.CharField(max_length=20, verbose_name="Nomor Telepon", unique=True)
    date_joined = models.DateField(auto_now_add=True, verbose_name="Tanggal Bergabung")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Anggota"
        verbose_name_plural = "Anggota"
        ordering = ['name']