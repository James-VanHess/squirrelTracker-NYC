#!/usr/bin/env python
# coding: utf-8


from django.urls import path
from . import views
from django.conf.urls import url
from .views import sightings_view, add_view, update_view, map_view, stats_view

app_name = 'sightings'
urlpatterns = [
    path('', views.sightings_view, name = 'sightings'),
    path('add/', views.add_view, name = 'add'),
    path('stats/', views.stats_view, name = 'stats'),
    path('<str:unique_squirrel_id>/', views.update_view, name = 'update'),
    path('map/', views.map_view, name = 'map'),
]

