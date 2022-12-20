from django.db import models


class BaseModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class SlugModel(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField(unique=True)

	class Meta:
		abstract = True
