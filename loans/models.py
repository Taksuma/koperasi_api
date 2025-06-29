from django.db import models
from members.models import Member # Import model Member

class Loan(models.Model):
    """
    Model untuk entitas Pinjaman.
    Mencatat informasi pinjaman yang diajukan oleh anggota.
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Disetujui'),
        ('rejected', 'Ditolak'),
        ('paid', 'Lunas'),
    ]

    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='loans', verbose_name="Anggota")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Jumlah Pinjaman")
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Tingkat Bunga (%)")
    term_months = models.IntegerField(verbose_name="Jangka Waktu (Bulan)")
    start_date = models.DateField(auto_now_add=True, verbose_name="Tanggal Mulai")
    end_date = models.DateField(blank=True, null=True, verbose_name="Tanggal Selesai") # Bisa dihitung setelah disetujui
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name="Status")

    def __str__(self):
        return f"Pinjaman {self.member.name} - {self.amount} ({self.status})"

    class Meta:
        verbose_name = "Pinjaman"
        verbose_name_plural = "Pinjaman"
        ordering = ['-start_date'] # Mengurutkan berdasarkan tanggal mulai terbaru

class LoanPayment(models.Model):
    """
    Model untuk entitas Pembayaran Pinjaman.
    Mencatat setiap angsuran pembayaran pinjaman.
    """
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='payments', verbose_name="Pinjaman")
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Jumlah Dibayar")
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name="Tanggal Pembayaran")
    description = models.TextField(blank=True, null=True, verbose_name="Deskripsi")

    def __str__(self):
        return f"Pembayaran untuk Pinjaman {self.loan.id} - {self.amount_paid}"

    class Meta:
        verbose_name = "Pembayaran Pinjaman"
        verbose_name_plural = "Pembayaran Pinjaman"
        ordering = ['-payment_date'] # Mengurutkan berdasarkan tanggal pembayaran terbaru