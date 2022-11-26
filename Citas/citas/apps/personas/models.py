from django.db import models

from apps.maestra.models import TablaMaestra

# Create your models here.

class Personas(models.Model):
    pers_nombre = models.CharField(max_length=30)
    pers_segundonombre = models.CharField(max_length=30)
    pers_apellido = models.CharField(max_length=20)
    pers_segundoapellido = models.CharField(max_length=20)
    pers_telefono = models.CharField(max_length=10)
    pers_correo = models.CharField(max_length=30)
    tiposexo = models.ForeignKey(TablaMaestra,related_name='tiposexo', null=True, blank=True, on_delete=models.CASCADE)
    tipodocumento = models.ForeignKey(TablaMaestra,related_name='tipodocumento', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return '{}'.format(self.pers_nombre)

class Cliente(models.Model):
    persona = models.ForeignKey(Personas, null=True, blank=True, on_delete=models.CASCADE)
    clie_nacionalidad = models.CharField(max_length=20)
    tipocliente = models.ForeignKey(TablaMaestra, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.clie_nacionalidad

class Empleado(models.Model):
    empl_nacionalidad = models.CharField(max_length=20)
    persona = models.ForeignKey(Personas, null=True, blank=True, on_delete=models.CASCADE)
    tipoempleado = models.ForeignKey(TablaMaestra, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.empl_nacionalidad