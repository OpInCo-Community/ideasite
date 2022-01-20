from django.db import models
from django.contrib.auth.models import AbstractUser

class TimeStampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True, default="")
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
