from django import forms
from django.db.models import fields
from .models import *

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class RegistroForm(forms.ModelForm):

    class Meta:
        model = Registro
        fields = '__all__'

class LoginForm(forms.ModelForm):

    class Meta:
        model = Login
        fields = '__all__'

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'