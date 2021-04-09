from django.forms import ModelForm
from .models import Squirrels


class Form(ModelForm):
    class Meta:
        model = Squirrel
        fields = '__all__'