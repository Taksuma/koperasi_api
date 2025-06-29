# File: koperasi_api/urls.py
"""
URL configuration for koperasi_api project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Hubungkan URL dari aplikasi API
    path('api/', include('members.urls')),
    path('api/', include('deposits.urls')),
    path('api/', include('loans.urls')),
]