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
    return render(request, 'SuperHeroes/details.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter ego')
        primary_power = request.POST.get('primary power')
        secondary_power = request.POST.get('secondary power')
        catch_phrase = request.POST.get('catch phrase')
        new_super = SuperHeroes(name=name, alter_ego=alter_ego, primary_power=primary_power, secondary_power=secondary_power, catch_phrase=catch_phrase)
        new_super.save()
        return HttpResponseRedirect(reverse('SuperHeroes:index'))
    else:
        return render(request, 'SuperHeroes/create.html')


def edit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter ego')
        primary_power = request.POST.get('primary power')
        secondary_power = request.POST.get('secondary power')
        catch_phrase = request.POST.get('catch phrase')
        edit_super = SuperHeroes(name=name, alter_ego=alter_ego, primary_power=primary_power,
                                secondary_power=secondary_power, catch_phrase=catch_phrase)
        edit_super.save()
        return HttpResponseRedirect(reverse('SuperHeroes:index'))
    else:
        return render(request, 'SuperHeroes/edit.html')


def remove_super(request, supers_id):
    one_super = SuperHeroes.objects.filter(pk=supers_id)
    if request.method == 'DELETE':
        one_super.remove(one_super)
        return HttpResponseRedirect(reverse('SuperHeroes:index'))
    else:
        return render(request, 'SuperHeroes/index.html', {'pk': one_super})


