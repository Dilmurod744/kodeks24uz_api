from django.db import models

from accounts.models import Account
from orders.models import shared
from products.models.products import Book


class Cart(shared.BaseModel):
	products = models.ManyToManyField(Book)
	client = models.ForeignKey(Account, models.CASCADE)

	class Meta:
		db_table = 'carts'


class Wishlist(shared.BaseModel):
	products = models.ManyToManyField(Book)
	client = models.ForeignKey(Account, models.CASCADE)

	class Meta:
		db_table = 'wishlists'


class Order(shared.BaseModel):
	client = models.ForeignKey(Account, related_name='orders', on_delete=models.PROTECT)
	amount_total = models.DecimalField(max_digits=10, decimal_places=2)
	address = models.CharField(max_length=250)
	city = models.CharField(max_length=150)
	payment_status = models.BooleanField(default=False)
	cart = models.OneToOneField(Cart, models.CASCADE)

	class Meta:
		db_table = 'orders'
		ordering = ('-created_at',)

	def __str__(self):
		return f'Order: №{str(self.id).zfill(6)}'

	def get_total_cost(self):
		return sum(product.get_cost() for product in self.cart.products.all())


class OrderItem(models.Model):
	order = models.ForeignKey(Order, related_name='order', on_delete=models.CASCADE)
	product = models.ForeignKey(Book, related_name='order_items', on_delete=models.PROTECT)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	quantity = models.PositiveIntegerField(default=1)

	def __str__(self):
		return self.id

	def get_cost(self):
		return self.price * self.quantity
