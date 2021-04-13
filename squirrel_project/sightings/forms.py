from django import forms
from django.forms import ModelForm
from .models import Squirrel


class django_form(forms.ModelForm):
    class Meta:
        model = Squirrel
        fields = '__all__'

