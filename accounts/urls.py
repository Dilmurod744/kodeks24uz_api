from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import LoginRefreshView

from accounts.views import LoginView, RegisterView, LogoutView

router = routers.DefaultRouter()

urlpatterns = [
	path('login/', LoginView.as_view(), name='auth_login'),
	path('login/refresh/', LoginRefreshView.as_view(), name='token_refresh'),
	path('register/', RegisterView.as_view(), name='auth_register'),
	path('logout/', LogoutView.as_view(), name='auth_logout'),

	path('', include(router.urls)),
]
