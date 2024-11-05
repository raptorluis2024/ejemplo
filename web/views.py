from django.shortcuts import render,HttpResponseRedirect
from .models import Flan
from .forms import ContactFormForm


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


def contacto(request):
    if request.method == "POST":
        form = ContactFormForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/")
    else:
        form = ContactFormForm()

    return render(request, "contactus.html", {"form":form})        

