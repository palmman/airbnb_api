from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('account/<int:pk>', views.AccountAPIView.as_view(), name='account' ),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('login/', views.MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('update_account/<int:pk>/', views.UpdateAccountView.as_view(), name='update_account'),
]


    
