from django.db import models

# Create your models here.


class TablaMaestra(models.Model):
    tama_nombre1 = models.CharField(max_length=30)
    tama_nombre2 = models.CharField(max_length=30)
    tama_dependencia1 = models.CharField(max_length=30)
    tama_dependencia2 = models.CharField(max_length=30)
    tama_codigo = models.CharField(max_length=30)
    tama_estado = models.CharField(max_length=30)

    def __str__(self) -> str:
        return '{}'.format(self.tama_nombre1)