from django import forms

from django import forms
from django.forms import ModelForm
from rolldice.models import Advert


class AdvertForm(ModelForm):
    class Meta:
        model = Advert