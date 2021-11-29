from django import forms
from django.db.models import fields
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'

class FormularioRegistro(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', "email", "password1", "password2"]

