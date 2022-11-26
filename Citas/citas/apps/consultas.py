import json
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from .factura.models import *
from .factura.serializers import *
from .maestra.models import *
from .personas.models import *
from django.db.models.functions import Lower
from django.core import serializers
from django_filters.rest_framework import DjangoFilterBackend


class Consulta1(ListAPIView):
    nombres = Factura.objects.all()
    serializer_class = FacturaSerializer
    
    def get(self, resquest, *args, **kwargs):
        data = Factura.objects.all().values('fact_nombre','fact_precio')
        response = {
            'cantidad': len(data)
        }
        return JsonResponse(response, safe=False)

class Consulta2(ListAPIView):
    queryset = Factura.objects.all().values('fact_nombre','fact_precio')
    serializer_class = FacturaSerializer

    def get(self, resquest, *args, **kwargs):
        registros = FacturaSerializer(self.get_queryset(), many=True)
        return Response(registros.data, status=status.HTTP_200_OK)

class Consulta3(ListAPIView):
    queryset = Agenda.objects.raw('SELECT id, agen_numero, agen_fecha FROM factura_agenda;')
    serializer_class = AgendaSerializer

    def get(self, resquest, *args, **kwargs):
        registros = AgendaSerializer(self.get_queryset(), many=True)
        return Response(registros.data, status=status.HTTP_200_OK)
