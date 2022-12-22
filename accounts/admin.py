from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from accounts.models import User


# Register your models here.
@admin.register(User)
class User(ImportExportModelAdmin):
	list_display = ('first_name', 'last_name', 'phone')
