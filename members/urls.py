# File: members/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MemberViewSet

# Buat router untuk mengelola URL dari ViewSet
router = DefaultRouter()
router.register(r'members', MemberViewSet, basename='member')

# URLConf untuk aplikasi members
urlpatterns = [
    path('', include(router.urls)),
]