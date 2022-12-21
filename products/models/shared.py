from django.db import models
from django.utils.text import slugify


class BaseModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class SlugModel(models.Model):
	name = models.CharField(max_length=150)
	slug = models.SlugField(unique=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(value=f'{self.name}-{self.id}')
		return super().save(*args, **kwargs)

	class Meta:
		abstract = True
