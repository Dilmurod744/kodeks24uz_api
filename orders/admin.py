from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from orders.models.orders import Order
from orders.models.products import Book


# Register your models here.
@admin.register(Book)
class Book(ImportExportModelAdmin):
	pass


@admin.register(Order)
class Order(ImportExportModelAdmin):
	pass
