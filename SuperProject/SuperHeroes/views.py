from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import SuperHeroes
from django.urls import reverse

# Create your views here.


def index(request):
    all_supers = SuperHeroes.objects.all()
    context = {
        'all_supers': all_supers
    }
    return render(request, 'SuperHeroes/index.html')


def detail(request, supers_id):
    one_entry = SuperHeroes.objects.get(pk=1)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        power = request.POST.get('power')
        new_super = SuperHeroes(name=name, power=power)
        new_super.save()
        return HttpResponseRedirect(reverse('SuperHeroes:index'))
    else:
        return render(request, 'SuperHeroes/create.html')