from rest_framework import serializers
from apps.factura.models import *
from ..maestra.serializers import TablaMaestraSerializer
from ..personas.serializers import *

class FacturaSerializer(serializers.ModelSerializer):
    tiposervicio = TablaMaestraSerializer(read_only=True)
    class Meta:
        model=Factura
        fields=('fact_nombre','fact_precio','tiposervicio')

class AgendaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)
    empleado = EmpleadoSerializer(read_only=True)
    factura = FacturaSerializer(read_only=True)
    class Meta:
        model= Agenda
        fields=('__all__')