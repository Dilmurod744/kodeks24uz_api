from rest_framework import generics, permissions, response, status
from rest_framework.views import APIView
from rest_framework_simplejwt import tokens, views

from accounts import models, serializers


class LoginView(views.TokenObtainPairView):
	permission_classes = (permissions.AllowAny,)
	serializer_class = serializers.TokenSerializer


class RegisterView(generics.CreateAPIView):
	queryset = models.User.objects.all()
	permission_classes = (permissions.AllowAny,)
	serializer_class = serializers.RegisterSerializer


class LogoutView(APIView):
	permission_classes = (permissions.IsAuthenticated,)

	def post(self, request):
		try:
			refresh_token = request.data["refresh_token"]
			token = tokens.RefreshToken(refresh_token)
			token.blacklist()

			return response.Response(status=status.HTTP_205_RESET_CONTENT)
		except Exception:
			return response.Response(status=status.HTTP_400_BAD_REQUEST)
