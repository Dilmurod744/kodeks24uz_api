from json import JSONEncoder, JSONDecoder

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from orders.models import shared


class Category(shared.SlugModel, shared.BaseModel):
	def _get_unique_slug(self):
		slug = slugify(self.name)
		unique_slug = slug
		num = 1
		while Category.objects.filter(slug=unique_slug).exists():
			unique_slug = '{}-{}'.format(slug, num)
			num += 1
		return unique_slug

	def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
		self.slug = self._get_unique_slug()
		if force_update is True:
			self.name = slugify(self.name)
		super().save(force_insert=False, force_update=False, using=None, update_fields=None)

	def __str__(self):
		return f'{self.name}'


class Book(shared.SlugModel, shared.BaseModel):
	class Language(models.TextChoices):
		UZB = 'uzb'
		UZB_RUS = 'uzb/rus'
		RUS = 'rus'
		CYR = 'cyr'
		ENG = 'eng'

	class Format(models.TextChoices):
		format_1 = '60х84 1/16'
		format_2 = '60×90 1/16'
		format_3 = '70×100 1/16'
		format_4 = '70×90 1/32'
		format_5 = '84х108 1/32'

	class Cover(models.TextChoices):
		HARD = 'hard'
		SOFT = 'soft'

	image = models.ImageField(upload_to='products/images/')
	price = models.DecimalField(max_digits=10, decimal_places=2)
	available = models.BooleanField(default=False)
	quantity = models.PositiveIntegerField(default=1)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
	full_title = models.CharField(max_length=150)
	description = models.CharField(max_length=1000)
	language = models.CharField(max_length=15, choices=Language.choices, default=Language.UZB)
	volume = models.IntegerField()
	format = models.CharField(max_length=15, choices=Format.choices, default=Format.format_1)
	ISBN = models.CharField(max_length=13, unique=True)
	cover = models.CharField(max_length=15, choices=Cover.choices, default=Cover.HARD)
	info = models.JSONField(encoder=JSONEncoder, decoder=JSONDecoder)

	def _get_unique_slug(self):
		slug = slugify(self.name)
		unique_slug = slug
		num = 1
		while Book.objects.filter(slug=unique_slug).exists():
			unique_slug = '{}-{}'.format(slug, num)
			num += 1
		return unique_slug

	def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
		self.slug = self._get_unique_slug()
		if force_update is True:
			self.name = slugify(self.name)
		super().save(force_insert=False, force_update=False, using=None, update_fields=None)

	class Meta:
		verbose_name = _("book")
		verbose_name_plural = _("books")
