from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reserva/', views.reserva, name='reserva'),
    path('registro/', views.registro, name='registro'),
    path('mantencion/', views.mantencion, name='mantencion'),
    path('contacto/', views.contacto, name='contacto'),
    path('departamento1/', views.departamento1, name='departamento1'),
    path('departamento2/', views.departamento2, name='departamento2'),
    path('departamento3/', views.departamento3, name='departamento3'),
    path('estadisticas/', views.estadisticas, name='estadisticas'),
    path('completado/', views.completado, name='completado'),
    path('check/', views.check, name='check'),
    path('checklist/', views.checklist, name='checklist'),
]