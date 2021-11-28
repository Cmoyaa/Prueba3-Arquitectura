from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reserva/', views.reserva, name='reserva'),
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('mantencion/', views.mantencion, name='mantencion'),
    path('contacto/', views.contacto, name='contacto'),
    path('departamento1/', views.departamento1, name='departamento1'),
    path('departamento2/', views.departamento2, name='departamento2'),
    path('departamento3/', views.departamento3, name='departamento3'),

]