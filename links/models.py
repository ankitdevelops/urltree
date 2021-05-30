from io import SEEK_END
from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import OneToOneField
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    link = models.URLField(blank=False)


