from django.db import models
from django.db.models.base import Model

opcionServExtra = [
    [0, "Transporte"],
    [1, "Cama extra"],
    [2, "Televisor extra"],
    [3, "Cocina eléctrica"],
]

opcionDepartamento = [
    [0,"Departamento 1, $300.000"],
    [1,"Departamento 2, $400.000"],
    [2,"Departamento 3, $550.000"],
]

opcionContacto = [
    [0,"Disponibilidad departamento"],
    [1,"Cancelar reserva"],
    [2,"Más información departamentos"],
    [3,"Dudas"],
    [4,"Quejas y/o reclamos"],
]

opcionPago = [
    [0,"Tarjeta de crédito"],
    [1,"Tarjeta de débito"],
    [2,"Paypal"],
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    telefono = models.CharField(max_length=12)
    tipo_contacto = models.IntegerField(choices=opcionContacto)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    fecha_arriendo = models.DateField()
    fecha_termino = models.DateField()
    acompanantes = models.IntegerField()
    departamento = models.IntegerField(choices=opcionDepartamento)
    servicio_extra = models.IntegerField(choices=opcionServExtra)
    metodo_de_pago = models.IntegerField(choices=opcionPago)

    def __str__(self):
        return self.nombre
