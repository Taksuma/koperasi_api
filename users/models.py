# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Kita bisa menambahkan field tambahan di sini jika perlu,
    # misalnya role, nomor telepon, dll.
    # Untuk sekarang, kita gunakan model bawaan yang sudah mencakup
    # username, password, email, first_name, last_name.
    
    # Menambahkan related_name untuk menghindari konflik dengan model User standar
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="user_set_custom",  # Nama yang unik
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="user_set_custom_permissions", # Nama yang unik
        related_query_name="user",
    )

    def __str__(self):
        return self.username