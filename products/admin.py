from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from products.models.products import Book, Category


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {"slug": ("name",)}


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
	list_display = ['image', 'name', 'price']
	prepopulated_fields = {"slug": ("name",)}
