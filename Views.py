#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import django
from django.db import DatabaseError
from django.db.models import Count, Avg, Max, Min
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.base import View
from django.views.generic.edit import CreateView, DeleteView
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.core.exceptions import ImproperlyConfigured
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import LoginView

from explorer import app_settings
from explorer.connections import connections
from explorer.exporters import get_exporter_class
from explorer.forms import QueryForm
from explorer.models import Query, QueryLog, MSG_FAILED_BLACKLIST
from explorer.tasks import execute_query
from explorer.utils import (
    url_get_rows,
    url_get_query_id,
    url_get_log_id,
    url_get_params,
    safe_login_prompt,
    fmt_sql,
    allowed_query_pks,
    url_get_show,
    url_get_fullscreen
)

from .models import #model_data
from .forms import #django_form


def sightings_view(request):
    view_data = model_data.objects.all()
    page = request.GET.get('page', 1)
    #optional
    paginator = Paginator(view_data, 50)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    #optional
    return render(request, 'sightings/sightings.html', {'users':users})


def add_view(request):
    if request.method == "POST":
        form = django_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/sightings/")
    else:
        form = django_form()
    return render(request, 'sightings/add.html', {'form':form})


def edit_view(request, unique_squirrel_id):
    edit_sighting = get_object_or_404(model_data, unique_squirrel_id = unique_squirrel_id)
    if request.method == "POST":
        form = django_form(request.POST, instance = edit_sighting)
        if form.is_valid():
            form.save()
            return redirect("/sightings/")
    form = django_form(instance=edit_sighting)
    return render(request, "sightings/edit.html", {"form": form, "unique_squirrel_id": unique_squirrel_id})


def stats_view(request):
    view_data = model_data.objects.all()
    total_squirrel = len(view_data)
    lat = view_data.aggregate(min_latitude = Min('latitude'),max_latitude = Max('latitude'),average_latitude = Avg('latitude'))
    lon = view_data.aggregate(min_longitude = Min('longitude'),max_longitude = Max('longitude'),average_longitude = Avg('longitude'))
    shift_count = list(view_data.values_list('shift').annotate(Count('shift')))
    age_count = list(view_data.values_list('age').annotate(Count('age')))
    fur_color = list(view_data.values_list('primary_fur_color').annotate(Count('primary_fur_color')))
    return render(request, 'sightings/stats.html', {"total_squirrel": total_squirrel,"lat": lat,"lon": lon,"shift_count": shift_count,"age_count": age_count,"fur_color": fur_color})


def map_view(request):
    sighting_limit = 100
    map_sighting = model_data.objects.all()[:sighting_limit]
    return render(request, 'map/map.html', {"map_sighting": map_sighting})

