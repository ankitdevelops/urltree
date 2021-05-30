from django import forms
from django.forms import ModelForm, fields
from . models import Link


class LinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ['title', 'link']

