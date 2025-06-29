from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from members.views import MemberViewSet
from deposits.views import DepositViewSet
from loans.views import LoanViewSet, LoanPaymentViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)

router = DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'deposits', DepositViewSet)
router.register(r'loans', LoanViewSet)
router.register(r'loan-payments', LoanPaymentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    # ... rute-rute aplikasi Anda yang sudah ada
    path('api/', include('members.urls')),
    path('api/', include('loans.urls')),
    path('api/', include('deposits.urls')),
]