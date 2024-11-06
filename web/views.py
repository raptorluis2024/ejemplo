from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .models import Flan
from .forms import ContactFormForm
from django.contrib.auth import login,logout, authenticate
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

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

@login_required
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

def log_in(request):
    template = loader.get_template('login.html')
    context = {'form':AuthenticationForm}
    if request.method == "GET":
        return HttpResponse(template.render(context, request))
    else:
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate( request, username=usuario, password=clave)
        if user is None:
            context["error"] = "Usuario o contraseña incorrectos"
            return HttpResponse(template.render(context, request))
        else:
            login(request, user)
            template = loader.get_template('flanes_privados.html')
            usuario = User.objects.filter(username=usuario).values()[0]["username"]
            context = {"user":usuario}
            return HttpResponseRedirect(template.render(context, request))
         
