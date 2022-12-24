from rest_framework import serializers

from products.models.products import Book


class ProductSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Book
		fields = ['name', 'slug', ]
