# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Daftarkan model User kustom Anda
admin.site.register(User, UserAdmin)