from django.urls import path
from accounts.views import LoginView, RegisterView
from rest_framework_simplejwt.views import LoginRefreshView

urlpatterns = [
	path('login/', LoginView.as_view(), name='auth_login'),
	path('login/refresh/', LoginRefreshView.as_view(), name='token_refresh'),
	path('register/', RegisterView.as_view(), name='auth_register'),

	# path('profile/', )
]
