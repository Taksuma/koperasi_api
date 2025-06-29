from django.db import models
from members.models import Member # Import model Member

class Deposit(models.Model):
    """
    Model untuk entitas Simpanan.
    Mencatat transaksi simpanan anggota.
    """
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='deposits', verbose_name="Anggota")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Jumlah Simpanan")
    deposit_date = models.DateTimeField(auto_now_add=True, verbose_name="Tanggal Simpanan")
    description = models.TextField(blank=True, null=True, verbose_name="Deskripsi")

    def __str__(self):
        return f"Simpanan {self.member.name} - {self.amount}"

    class Meta:
        verbose_name = "Simpanan"
        verbose_name_plural = "Simpanan"
        ordering = ['-deposit_date'] # Mengurutkan berdasarkan tanggal simpanan terbaru
