from json import JSONEncoder, JSONDecoder

from django.db import models
from django.utils.translation import gettext_lazy as _

from orders.models import shared


class Image(models.Model):
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to='images', blank=True)

	def __str__(self):
		return self.title


class Book(shared.SlugModel, shared.BaseModel):
	class Category(models.TextChoices):
		CODEX = 'codex'
		TEXTBOOK = 'textbook'
		LAW = 'law'
		OTHER = 'other'

	class Language(models.TextChoices):
		UZB = 'uzb'
		UZB_RUS = 'uzb/rus'
		RUS = 'rus'

	class Format(models.TextChoices):
		format_1 = '60×90 1/16'

	class Cover(models.TextChoices):
		HARD = 'hard'
		SOFT = 'soft'

	image = models.ImageField(upload_to='products/images/')
	title = models.CharField()
	price = models.FloatField()
	available = models.BooleanField()
	category = models.CharField(choices=Category)
	full_title = models.CharField()
	description = models.CharField(max_length=255)
	language = models.CharField(choices=Language)
	volume = models.IntegerField()
	format = models.CharField(choices=Format)
	ISBN = models.CharField(max_length=13, unique=True)
	cover = models.CharField(choices=Cover)
	info = models.JSONField(encoder=JSONEncoder, decoder=JSONDecoder)

	class Meta:
		verbose_name = _("book")
		verbose_name_plural = _("books")
