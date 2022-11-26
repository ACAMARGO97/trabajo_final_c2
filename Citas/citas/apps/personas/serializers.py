from apps.maestra.serializers import TablaMaestraSerializer
from rest_framework import serializers
from apps.personas.models import *

class PersonasSerializer(serializers.ModelSerializer):
    tiposexo = TablaMaestraSerializer(read_only=True)
    tipodocumento = TablaMaestraSerializer(read_only=True)
    class Meta:
        model=Personas
        fields=('__all__')

class EmpleadoSerializer(serializers.ModelSerializer):
    persona = PersonasSerializer(read_only=True)
    class Meta:
        model= Empleado
        fields=('__all__')

class ClienteSerializer(serializers.ModelSerializer):
    persona = PersonasSerializer(read_only=True)
    class Meta:
        model=Cliente
        fields=('__all__')