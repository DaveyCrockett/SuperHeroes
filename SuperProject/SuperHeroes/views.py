from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import SuperHeroes
from django.urls import reverse
from django.views.generic import View

# Create your views here.


def index(request):
    all_supers = SuperHeroes.objects.all()
    context = {
        'all_supers': all_supers
    }
    return render(request, 'SuperHeroes/index.html', context)


def details(request, supers_id):
    one_super = SuperHeroes.objects.get(pk=supers_id)
    context = {
        'one_super': one_super
    }
    if request.method == 'POST':
        one_super.name = request.POST.get('name')
        one_super.alter_ego = request.POST.get('alter_ego')
        one_super.primary_power = request.POST.get('primary_power')
        one_super.secondary_power = request.POST.get('secondary_power')
        one_super.catch_phrase = request.POST.get('catch_phrase')
        edit_super = SuperHeroes(id=supers_id, name=one_super.name, alter_ego=one_super.alter_ego, primary_power=one_super.primary_power,
                                secondary_power=one_super.secondary_power, catch_phrase=one_super.catch_phrase)
        edit_super.save()
        return HttpResponseRedirect(reverse('SuperHeroes:index'))
    else:
        return render(request, 'SuperHeroes/details.html', context)


def create(request):
    all_supers = SuperHeroes.objects.all()
    all_sups_id = all_supers.last().id
    if request.method == 'POST':
        id = all_sups_id + 1
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_power = request.POST.get('primary_power')
        secondary_power = request.POST.get('secondary_power')
        catch_phrase = request.POST.get('catch_phrase')
        new_super = SuperHeroes(id=id, name=name, alter_ego=alter_ego, primary_power=primary_power, secondary_power=secondary_power, catch_phrase=catch_phrase)
        new_super.save()
        return HttpResponseRedirect(reverse('SuperHeroes:index'))
    else:
        return render(request, 'SuperHeroes/create.html')


def remove_super(request, supers_id):
    SuperHeroes.objects.filter(pk=supers_id).delete()
    return HttpResponseRedirect(reverse('SuperHeroes:index'))



