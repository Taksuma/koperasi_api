# koperasi_api/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from members.views import MemberViewSet
from deposits.views import DepositViewSet
from loans.views import LoanViewSet, LoanPaymentViewSet
from users.views import UserViewSet  # Impor UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'deposits', DepositViewSet)
router.register(r'loans', LoanViewSet)
router.register(r'loan-payments', LoanPaymentViewSet)
router.register(r'users', UserViewSet)  # Daftarkan users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
]