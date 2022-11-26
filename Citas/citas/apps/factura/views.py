from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from apps.factura.models import *
from apps.factura.serializers import *

##Factura CRUD
class FacturaView(ListAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

    def get(self, request, *args, **kwargs):
        facturaData = FacturaSerializer(self.get_queryset(), many=True)
        return Response(facturaData.data, status=status.HTTP_200_OK)

class FacturaViewOwner(ListAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

    def get(self, request, *args, **kwargs):
        facturaData = FacturaSerializer(self.get_queryset(), many=True)
        return Response(facturaData.data, status=status.HTTP_200_OK)

class FacturaCreate(CreateAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

    def post(self, request, *args, **kwargs):
        createData = FacturaSerializer(data=request.data)
        if createData.is_valid():
            createData.save()
            return Response(createData.data, status=status.HTTP_200_OK)
        return Response(createData.errors, status=status.HTTP_400_BAD_REQUEST)

class FacturaUpdate(UpdateAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class FacturaDelete(DestroyAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer


##Agenda CRUD
class AgendaView(ListAPIView):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

    def get(self, request, *args, **kwargs):
        agendaData = AgendaSerializer(self.get_queryset(), many=True)
        return Response(agendaData.data, status=status.HTTP_200_OK)

class AgendaViewOwner(ListAPIView):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

    def get(self, request, *args, **kwargs):
        agendaData = AgendaSerializer(self.get_queryset(), many=True)
        return Response(agendaData.data, status=status.HTTP_200_OK)

class AgendaCreate(CreateAPIView):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

    def post(self, request, *args, **kwargs):
        createData = AgendaSerializer(data=request.data)
        if createData.is_valid():
            createData.save()
            return Response(createData.data, status=status.HTTP_200_OK)
        return Response(createData.errors, status=status.HTTP_400_BAD_REQUEST)

class AgendaUpdate(UpdateAPIView):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

class AgendaDelete(DestroyAPIView):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer