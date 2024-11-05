from django.shortcuts import render
from .models import Flan


def indice(request):
    return render(request, 'index.html', {})

def acerca(request):
    return render(request, 'about.html', {})

def bienvenido(request):
    return render(request, 'welcome.html', {})

def flanes_publicos(request):
    flanes = Flan.objects.filter(is_private = False)
    context = {"flanes": flanes}
    return render(request, 'flanes_publicos.html', context)

def flanes_privados(request):
    flanes = Flan.objects.filter(is_private = True)
    context = {"flanes": flanes}
    return render(request, 'flanes_privados.html', context)
