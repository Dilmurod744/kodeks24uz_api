from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class AccountManager(BaseUserManager):
	def create_user(self, username, email, phone, password, **extra_fields):
		user = self.validate(username, email, phone, password, **extra_fields)
		return user

	def create_superuser(self, username, email, phone, password, **extra_fields):
		extra_fields.setdefault("is_staff", True)
		extra_fields.setdefault("is_superuser", True)
		extra_fields.setdefault("is_active", True)
		extra_fields.setdefault("type", Account.Type.ADMIN)

		user = self.validate(username, email, phone, password, **extra_fields)
		return user

	def validate(self, username, email, phone, password, **extra_fields):
		if not username:
			raise ValueError('The given Username must be set')

		if not email:
			raise ValueError('The given Email must be set')

		if not phone:
			raise ValueError('The given PhoneNumber must be set')

		if not extra_fields['first_name']:
			raise ValueError('The given FirstName must be set')

		if not extra_fields['last_name']:
			raise ValueError('The given LastName must be set')

		email = self.normalize_email(email)
		user = self.model(username=username, email=email, phone=phone, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)

		return user


class Account(AbstractUser):
	class Type(models.TextChoices):
		ADMIN = 'admin'
		CEO = 'ceo'
		EMPLOYEE = 'employee'
		USER = 'user'

	# email = models.CharField(max_length=150, unique=True)
	phone = models.CharField(max_length=13, unique=True)
	type = models.CharField(max_length=20, choices=Type.choices, default=Type.USER)

	objects = AccountManager()

	REQUIRED_FIELDS = ['email', 'phone', 'first_name', 'last_name']

	class Meta(AbstractUser.Meta):
		verbose_name = _("account")
		verbose_name_plural = _("accounts")
		ordering = ('first_name', 'last_name')
		swappable = 'AUTH_USER_MODEL'

	def __str__(self):
		return f'{self.first_name}, {self.last_name}'
