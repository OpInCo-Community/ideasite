from django.db import models
from django.contrib.auth import get_user_model
from core.models import TimeStampedModel
# Create your models here.
from django.template.defaultfilters import slugify
from django.utils.crypto import get_random_string


class Idea(TimeStampedModel):
    title = models.CharField(max_length=256)
    description = models.TextField(default="", blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    slug = models.SlugField(default="", blank=True)

    def __str__(self):
        return f'{self.title} - {self.author.username}'

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = f'{slugify(self.title)}-'+get_random_string(length=4)

        super().save(*args, **kwargs)
