from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics

from accounts.models import User
from accounts.serializers import TokenSerializer, RegisterSerializer


class TokenView(TokenObtainPairView):
	permission_classes = (AllowAny,)
	serializer_class = TokenSerializer


class RegisterView(generics.CreateAPIView):
	queryset = User.objects.all()
	permission_classes = (AllowAny,)
	serializer_class = RegisterSerializer
