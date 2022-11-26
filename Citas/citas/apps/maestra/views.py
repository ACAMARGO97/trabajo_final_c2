from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from apps.maestra.models import *
from apps.maestra.serializers import *

##Tabla Maestra CRUD
class TablaMaestraView(ListAPIView):
    queryset = TablaMaestra.objects.all()
    serializer_class = TablaMaestraSerializer

    def get(self, request, *args, **kwargs):
        maestraData = TablaMaestraSerializer(self.get_queryset(), many=True)
        return Response(maestraData.data, status=status.HTTP_200_OK)

class TablaMaestraViewOwner(ListAPIView):
    queryset = TablaMaestra.objects.all()
    serializer_class = TablaMaestraSerializer

    def get(self, request, *args, **kwargs):
        maestraData = TablaMaestraSerializer(self.get_queryset(), many=True)
        return Response(maestraData.data, status=status.HTTP_200_OK)

class TablaMaestraCreate(CreateAPIView):
    queryset = TablaMaestra.objects.all()
    serializer_class = TablaMaestraSerializer

    def post(self, request, *args, **kwargs):
        createData = TablaMaestraSerializer(data=request.data)
        if createData.is_valid():
            createData.save()
            return Response(createData.data, status=status.HTTP_200_OK)
        return Response(createData.errors, status=status.HTTP_400_BAD_REQUEST)

class TablaMaestraUpdate(UpdateAPIView):
    queryset = TablaMaestra.objects.all()
    serializer_class = TablaMaestraSerializer

class TablaMaestraDelete(DestroyAPIView):
    queryset = TablaMaestra.objects.all()
    serializer_class = TablaMaestraSerializer