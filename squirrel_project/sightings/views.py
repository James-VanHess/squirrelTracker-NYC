#!/usr/bin/env python
# coding: utf-8



import django
from django.db import DatabaseError
from django.db.models import Count, Avg, Max, Min
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from django.views.generic.base import View
from django.views.generic.edit import CreateView, DeleteView
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.core.exceptions import ImproperlyConfigured
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import LoginView


from .models import Squirrel
from .forms import django_form


def sightings_view(request):
    view_data = Squirrel.objects.all()
    paginator = Paginator(view_data, 36)

    page = request.GET.get('page')
    view_data = paginator.get_page(page)
    context = {'squirrel':view_data}
   
    return render(request, 'sightings/Sightings_HTML.html', context)


def add_view(request):
    if request.method == "POST":
        form = django_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/sightings/")
    else:
        form = django_form()
    return render(request, 'sightings/Add_HTML.html', {'form':form})


def update_view(request, unique_squirrel_id):
    update_sighting = get_object_or_404(Squirrel, unique_squirrel_id = unique_squirrel_id)
    if request.method == "POST":
        form = django_form(request.POST, instance = update_sighting)
        if form.is_valid():
            form.save()
            return redirect("/sightings/")
    form = django_form(instance=update_sighting)
    return render(request, "sightings/Update_HTML.html", {"form": form, "unique_squirrel_id": unique_squirrel_id})


def stats_view(request):
    view_data = Squirrel.objects.all()
    total_squirrel = len(view_data)
    lat = view_data.aggregate(min_latitude = Min('latitude'),max_latitude = Max('latitude'),average_latitude = Avg('latitude'))
    lon = view_data.aggregate(min_longitude = Min('longitude'),max_longitude = Max('longitude'),average_longitude = Avg('longitude'))
    shift_count = list(view_data.values_list('shift').annotate(Count('shift')))
    age_count = list(view_data.values_list('age').annotate(Count('age')))
    fur_color = list(view_data.values_list('primary_fur_color').annotate(Count('primary_fur_color')))
    return render(request, 'sightings/Stats_HTML.html', {"total_squirrel": total_squirrel,"lat": lat,"lon": lon,"shift_count": shift_count,"age_count": age_count,"fur_color": fur_color})


def map_view(request):
    sighting_limit = 100
    map_sighting = Squirrel.objects.all()[:sighting_limit]
    return render(request, 'sightings/Map_HTML.html', {"map_sighting": map_sighting})

