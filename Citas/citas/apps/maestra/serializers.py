from rest_framework import serializers
from apps.maestra.models import *

class TablaMaestraSerializer(serializers.ModelSerializer):
    class Meta:
        model = TablaMaestra
        fields =('__all__')