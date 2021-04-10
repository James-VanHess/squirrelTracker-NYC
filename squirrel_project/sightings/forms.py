#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from django.forms import ModelForm
from .models import Squirrel


class django_form(forms. ModelForm):
    class Meta:
        model = Squirrel
        fields = '__all__'

