from django.db import models

from accounts.models import User
from orders.models.shared import BaseModel
from orders.models.products import Book


class Cart(BaseModel):
	products = models.ManyToManyField(Book)
	client = models.ForeignKey(User, models.CASCADE)

	class Meta:
		db_table = 'carts'


class Wishlist(BaseModel):
	products = models.ManyToManyField(Book)
	client = models.ForeignKey(User, models.CASCADE)

	class Meta:
		db_table = 'wishlists'


class Order(BaseModel):
	address = models.CharField(max_length=250)
	city = models.CharField(max_length=100)
	paid = models.BooleanField(default=False)
	cart = models.OneToOneField(Cart, models.CASCADE)

	class Meta:
		db_table = 'orders'
		ordering = ('-created_at',)

	def __str__(self):
		return 'Order: ' + '№' + str(self.id).zfill(6)

	def get_total_cost(self):
		return sum(product.get_cost() for product in self.cart.products.all())


class OrderItem(models.Model):
	order = models.ForeignKey(Order, related_name='order', on_delete=models.CASCADE)
	product = models.ForeignKey(Book, related_name='ordered_items', on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	quantity = models.PositiveIntegerField(default=1)

	class Meta:
		abstract = True

	def __str__(self):
		return str(self.id)

	def get_cost(self):
		return self.price * self.quantity
