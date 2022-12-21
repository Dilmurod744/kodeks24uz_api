from json import JSONEncoder, JSONDecoder

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from products.models import shared


class Category(shared.SlugModel, shared.BaseModel):

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
		format_1 = '60x84 1/32'
		format_2 = '60x90 1/32'
		format_3 = '70x90 1/32'
		format_4 = '70x100 1/32'
		format_5 = '70x108 1/32'
		format_6 = '75x90 1/32'
		format_7 = '84x108 1/32'

	# format_1 = '60x84 1/16'
	# format_2 = '60x90 1/16'
	# format_3 = '70x90 1/16'
	# format_4 = '70x100 1/16'
	# format_5 = '70x108 1/16'
	# format_6 = '75x90 1/16'
	# format_7 = '84x108 1/16'

	class Cover(models.TextChoices):
		HARD = 'hard'
		SOFT = 'soft'

	image = models.ImageField(upload_to=f'products/images/')
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

	class Meta:
		verbose_name = _("book")
		verbose_name_plural = _("books")
