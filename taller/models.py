from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nombre


class Reparacion(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='reparaciones'
    )
    descripcion = models.CharField(max_length=150)
    costo = models.PositiveIntegerField()
    fecha = models.DateField()
    terminada = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.descripcion} - {self.cliente.nombre}"