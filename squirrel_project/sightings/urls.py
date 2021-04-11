#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from django.urls import path
from . import views
from django.conf.urls import url
from .views import sightings_view, add_view, update_view, map_view, stats_view

directory = 'sightings'
urlpatterns = [
    path('', views.sightings_view, name ='sightings'),
    path('sightings/', views.sightings_view, name='sightings'),
    path('sightings/add/', views.add_view, name = 'add'),
    path('sightings/stats/', views.stats_view, name = 'stats'),
    path('sightings/update/<str:squirrel_id>/', views.update_view, name = 'update'),
    path('sightings/map/', views.map_view, name = 'map'),
]

