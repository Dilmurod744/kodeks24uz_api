from rest_framework import generics, permissions, viewsets
from rest_framework_simplejwt import views

from accounts import models, serializers
from accounts.serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
	queryset = models.Account.objects.all().order_by('-date_joined')
	serializer_class = AccountSerializer
	permission_classes = [permissions.IsAdminUser]


class LoginView(views.TokenObtainPairView):
	permission_classes = (permissions.AllowAny,)
	serializer_class = serializers.LoginSerializer


class RegisterView(generics.CreateAPIView):
	queryset = models.Account.objects.all()
	permission_classes = (permissions.AllowAny,)
	serializer_class = serializers.RegisterSerializer


class ChangePasswordView(generics.UpdateAPIView):
	queryset = models.Account.objects.all()
	permission_classes = (permissions.IsAuthenticated,)
	serializer_class = serializers.ChangePasswordSerializer


class UpdateProfileView(generics.UpdateAPIView):
	queryset = models.Account.objects.all()
	permission_classes = (permissions.IsAuthenticated,)
	serializer_class = serializers.UpdateUserSerializer
