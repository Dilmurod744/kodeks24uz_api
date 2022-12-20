from django.urls import path
from accounts.views import TokenView, RegisterView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
	path('login/', TokenView.as_view(), name='auth_login'),
	path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
	path('register/', RegisterView.as_view(), name='auth_register'),
]
