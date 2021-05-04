from django import forms
from django.forms import ModelForm, fields
from . models import Link, BackgroundImage


class LinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ['title', 'link']

class ImageForm(ModelForm):
    class Meta:
        model = BackgroundImage
        fields = ['image_url',]