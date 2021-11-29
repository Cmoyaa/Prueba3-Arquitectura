from django.contrib import messages
from django.contrib.auth.forms import UserModel, UsernameField
from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request, 'paginas/home.html')

@login_required(login_url='/accounts/login')
def reserva(request):
    data = {
        'form': ReservaForm()
    }
    current_user = request.user
    print (current_user)
    if request.method == 'POST':
        reserva = ReservaForm(data=request.POST)
        if  User.is_active and reserva.is_valid():
            reserva.save()
            return render(request, 'paginas/completado.html'    )
        else:
            data["form"] = reserva
    return render(request, 'paginas/reserva.html', data)

def registro(request):
    data = {
        'form':FormularioRegistro()
    }

    if request.method == 'POST':
        formulario = FormularioRegistro(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

def mantencion(request):
    return render(request, 'paginas/mantencion.html')

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        
        if formulario.is_valid():
            formulario.save()
            data["Mensaje"] = "Formulario Enviado"
        else:
            data["form"] = formulario
    return render(request, 'paginas/contacto.html', data)

def departamento1(request):
    return render(request, 'paginas/departamentos/departamento1.html')

def departamento2(request):
    return render(request, 'paginas/departamentos/departamento2.html')

def departamento3(request):
    return render(request, 'paginas/departamentos/departamento3.html')

@login_required(login_url='/accounts/login')
def estadisticas(request):
    return render(request, 'paginas/estadisticas.html')

def completado(request):
    return render(request, 'paginas/completado.html')

def check(request):
    return render(request, 'paginas/check.html')

def checklist(request):
    return render(request, 'paginas/checklist.html')