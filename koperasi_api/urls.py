# koperasi_api/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Impor semua ViewSet dari aplikasi Anda
from users.views import UserViewSet
from members.views import MemberViewSet
from deposits.views import DepositViewSet
from loans.views import LoanViewSet, LoanPaymentViewSet

# Buat satu router utama untuk seluruh proyek
router = DefaultRouter()

# Daftarkan setiap ViewSet ke router
router.register(r'users', UserViewSet, basename='user')
router.register(r'members', MemberViewSet)
router.register(r'deposits', DepositViewSet)
router.register(r'loans', LoanViewSet)
router.register(r'loan-payments', LoanPaymentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Endpoint untuk login dan mendapatkan token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Sertakan semua URL yang dibuat otomatis oleh router
    # Ini akan membuat endpoint seperti /api/users/, /api/members/, dll.
    path('api/', include(router.urls)),
]