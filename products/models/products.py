from json import JSONEncoder, JSONDecoder

from django.db import models
from django.utils.translation import gettext_lazy as _

from products.models import shared


class Category(shared.SlugModel, shared.BaseModel):
	class Meta:
		verbose_name = _("category")
		verbose_name_plural = _("categories")

	def __str__(self):
		return self.name


class Book(shared.SlugModel, shared.BaseModel):
	class Language(models.TextChoices):
		UZB_RUS = 'uzb/rus'
		UZB = 'uzb'
		RUS = 'rus'
		CYR = 'cyr'
		ENG = 'eng'

	class Format(models.TextChoices):
		format_01 = '60x84 1/32'
		format_02 = '60x90 1/32'
		format_03 = '70x90 1/32'
		format_04 = '70x100 1/32'
		format_05 = '70x108 1/32'
		format_06 = '75x90 1/32'
		format_07 = '84x108 1/32'
		format_08 = '60x84 1/16'
		format_09 = '60x90 1/16'
		format_10 = '70x90 1/16'
		format_11 = '70x100 1/16'
		format_12 = '70x108 1/16'
		format_13 = '75x90 1/16'
		format_14 = '84x108 1/16'

	class Cover(models.TextChoices):
		HARD = 'hard'
		SOFT = 'soft'

	image = models.ImageField(max_length=150, upload_to=f'products/images/')

	price = models.DecimalField(max_digits=10, decimal_places=2)
	available = models.BooleanField(default=True)
	quantity = models.PositiveIntegerField(default=1)
	category = models.ForeignKey(Category, on_delete=models.RESTRICT, null=True)

	full_title = models.CharField(max_length=150)
	description = models.CharField(max_length=1000)

	language = models.CharField(max_length=15, choices=Language.choices, default=Language.UZB)
	volume = models.PositiveIntegerField()
	format = models.CharField(max_length=15, choices=Format.choices, default=Format.format_01)
	ISBN = models.CharField(max_length=13, unique=True)
	cover = models.CharField(max_length=15, choices=Cover.choices, default=Cover.HARD)

	info = models.JSONField(encoder=JSONEncoder, decoder=JSONDecoder, null=True, blank=True)

	class Meta:
		verbose_name = _("book")
		verbose_name_plural = _("books")

	def __str__(self):
		return self.name
