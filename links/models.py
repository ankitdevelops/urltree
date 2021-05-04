from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import OneToOneField

# Create your models here.

class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    link = models.URLField(blank=False)

class BackgroundImage(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE)
    image_url = models.URLField()