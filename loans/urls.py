# File: loans/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoanViewSet, LoanPaymentViewSet

router = DefaultRouter()
router.register(r'loans', LoanViewSet, basename='loan')
router.register(r'loan-payments', LoanPaymentViewSet, basename='loan-payment')

urlpatterns = [
    path('', include(router.urls)),
]