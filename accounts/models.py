from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class UserManager(BaseUserManager):
	def create_user(self, username, email, phone, password, **extra_fields):
		if not username:
			raise ValueError(_('The Username must be set'))

		if not email:
			raise ValueError(_('The Email must be set'))

		if not phone:
			raise ValueError(_('The PhoneNumber must be set'))

		"""
		if not first_name:
			raise ValueError(_('The PhoneNumber must be set'))
		
		if not last_name:
			raise ValueError(_('The PhoneNumber must be set'))
		"""

		email = self.normalize_email(email)
		user = self.model(username=username, email=email, phone=phone, **extra_fields)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, username, email, phone, password, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_active', True)
		extra_fields.setdefault('type', User.Type.ADMIN)

		if not username:
			raise ValueError(_('The Username must be set'))

		if not email:
			raise ValueError(_('The Email must be set'))

		if not phone:
			raise ValueError(_('The PhoneNumber must be set'))

		if extra_fields.get('is_staff') is not True:
			raise ValueError(_('Superuser must have is_staff=True.'))

		if extra_fields.get('is_superuser') is not True:
			raise ValueError(_('Superuser must have is_superuser=True.'))

		email = self.normalize_email(email)
		user = self.model(username=username, email=email, phone=phone, **extra_fields)
		user.set_password(password)
		user.save()

		return user


class User(AbstractUser):
	class Type(models.TextChoices):
		ADMIN = 'admin'
		CEO = 'ceo'
		EMPLOYEE = 'employee'
		USER = 'user'

	phone = models.CharField(max_length=13, unique=True)
	type = models.CharField(max_length=20, choices=Type.choices, default=Type.USER)

	objects = UserManager()

	REQUIRED_FIELDS = ['email', 'phone', 'first_name', 'last_name']

	class Meta:
		swappable = 'AUTH_USER_MODEL'
