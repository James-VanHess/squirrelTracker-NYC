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
    return render(request, 'sightings/Sightings_HTML.html', {'users':users})
    
    # view_data = Squirrel.objects.all()[:50]
    # context = {'sightings':view_data}
    # return render(request, 'sightings/Sightings_HTML.html', context)


def add_view(request):
    if request.method == "POST":
        form = django_form(request.POST)
        if form.is_valid():
            #x = form['unique_squirrel_id'].value()
            form.save()
            return redirect("/sightings/")
    else:
        form = django_form()
    return render(request, 'sightings/Add_HTML.html', {'form':form})


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
        return render(request,'sightings/Update_HTML.html',context)
    
    # update_sighting = get_object_or_404(Squirrel, unique_squirrel_id = unique_squirrel_id)
    # if request.method == "POST":
    #     form = django_form(request.POST, instance = update_sighting)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("/sightings/")
    # form = django_form(instance=update_sighting)
    # return render(request, "sightings/Update_HTML.html", {"form": form, "unique_squirrel_id": unique_squirrel_id})


def stats_view(request):
    return render(request, 'sightings/Stats_HTML.html')


def map_view(request):
    sighting_limit = 100
    map_sighting = Squirrel.objects.all()[:sighting_limit]
    return render(request, 'sightings/Map_HTML.html', {"map_sighting": map_sighting})

