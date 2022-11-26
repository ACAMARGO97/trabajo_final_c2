from django.db import models
from apps.maestra.models import *

from apps.personas.models import Cliente, Empleado

# Create your models here.


class Factura(models.Model):
    fact_nombre = models.CharField(max_length=20)
    fact_precio = models.BigIntegerField()
    tiposervicio = models.ForeignKey(TablaMaestra, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return '{}'.format(self.fact_nombre, self.fact_precio, self.tiposervicio)

class Agenda(models.Model):
    agen_numero = models.CharField(max_length=20)
    agen_fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, null=True, blank=True, on_delete=models.CASCADE)
    factura = models.ForeignKey(Factura, null=True, blank=True, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.agen_numero
