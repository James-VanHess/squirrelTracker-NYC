import json
import django
from django.db import DatabaseError
from django.db.models import Count, Avg, Max, Min
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, ListView
from django.views.generic.base import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.core.exceptions import ImproperlyConfigured
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import LoginView


from sightings.models import Squirrel
from sightings.forms import django_form


def sightings_view(request):
    sq_data=Squirrel.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(sq_data, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'sightings/sightings_HTML.html', {'users':users})
    

def add_view(request):
    if request.method == "POST":
        form = django_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/sightings/")
    else:
        form = django_form()
    return render(request, 'sightings/add_HTML.html', {'form':form})


def update_view(request, unique_squirrel_id):
    Object = get_object_or_404(Squirrel,unique_squirrel_id=unique_squirrel_id)
    form = django_form(request.POST or None,instance=Object)
    context = {'form':form}
    if form.is_valid():
        Object=form.save(commit=False)
        Object.save()
        return redirect('/sightings/')
    else:
        context={
                'form':form,
        }
        return render(request,'sightings/update_HTML.html',context)
    

def stats_view(request):
    sq_data = Squirrel.objects.all()
    total = len(sq_data)
    lat = sq_data.aggregate(min_latitude=Min('latitude'),max_latitude=Max('latitude'),average_latitude=Avg('latitude'))
    lon = sq_data.aggregate(min_longitude=Min('longitude'),max_longitude=Max('longitude'),average_longitude=Avg('longitude'))
    shift = list(sq_data.values_list('shift').annotate(Count('shift')))
    age = list(sq_data.values_list('age').annotate(Count('age')))
    fur = list(sq_data.values_list('primary_fur_color').annotate(Count('primary_fur_color')))
    return render(request, 'sightings/stats_HTML.html', {"total":total,"lat":lat,"lon":lon,"shift":shift,"age":age,"fur":fur})
    


def map_view(request):
    map_squirrel = Squirrel.objects.all()[:100]
    return render(request, 'sightings/map_HTML.html', {"map_squirrel": map_squirrel})