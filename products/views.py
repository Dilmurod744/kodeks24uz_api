from rest_framework import viewsets, permissions

from products.models.products import Book
from products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = ProductSerializer
	permission_classes = [permissions.IsAuthenticated]
	http_method_names = ['get',]
