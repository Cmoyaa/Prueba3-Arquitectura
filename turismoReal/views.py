from django.shortcuts import render
from .forms import *

def home(request):
    return render(request, 'paginas/home.html')

def reserva(request):
    data = {
        'form': ReservaForm()
    }

    if request.method == 'POST':
        reserva = ReservaForm(data=request.POST)
        if reserva.is_valid():
            reserva.save()
            data["Mensaje"] = "Reserva creada correctamente"
        else:
            data["form"] = reserva
    return render(request, 'paginas/reserva.html', data)
    
def login(request):
    data = {
        'form': LoginForm()
    }

    if request.method == 'POST':
        login = LoginForm(data=request.POST)
        if login.is_valid():
            login.save()
            data["Mensaje"] = "Inicio de sesión correcto"
        else:
            data["form"] = login
    return render(request, 'paginas/login.html', data)

def registro(request):
    data = {
        'form': RegistroForm()
    }

    if request.method == 'POST':
        registro = RegistroForm(data=request.POST)
        if registro.is_valid():
            registro.save()
            data["Mensaje"] = "Registro Completado"
        else:
            data["form"] = registro
    return render(request, 'paginas/registro.html', data)

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
    


