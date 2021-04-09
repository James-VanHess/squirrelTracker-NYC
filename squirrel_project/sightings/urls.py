#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from django.urls import path

from . import views

directory = 'sightings'
url_list = [
    path('', views.sightings_view, name = 'sightings'),
    path('add/', views.add_view, name = 'add'),
    path('stats/', views.stats_view, name = 'stats'),
    path('<str:unique_squirrel_id>/', views.update_view, name = 'update'),
    path('', views.map, name = 'map'),
]

