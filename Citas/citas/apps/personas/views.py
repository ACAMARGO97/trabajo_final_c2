from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from apps.personas.models import *
from apps.personas.serializers import *

##Personas CRUD

class PersonasView(ListAPIView):
    queryset = Personas.objects.all()
    serializer_class = PersonasSerializer

    def get(self, request, *args, **kwargs):
        personaData = PersonasSerializer(self.get_queryset(), many=True)
        return Response(personaData.data, status=status.HTTP_200_OK)

class PersonasViewOwner(ListAPIView):
    queryset = Personas.objects.all()
    serializer_class = PersonasSerializer

    def get(self, request, *args, **kwargs):
        personaData = PersonasSerializer(self.get_queryset(), many=True)
        return Response(personaData.data, status=status.HTTP_200_OK)

class PersonasCreate(CreateAPIView):
    queryset = Personas.objects.all()
    serializer_class = PersonasSerializer

    def post(self, request, *args, **kwargs):
        createData = PersonasSerializer(data=request.data)
        if createData.is_valid():
            createData.save()
            return Response(createData.data, status=status.HTTP_200_OK)
        return Response(createData.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonasUpdate(UpdateAPIView):
    queryset = Personas.objects.all()
    serializer_class = PersonasSerializer


class PersonasDelete(DestroyAPIView):
    queryset = Personas.objects.all()
    serializer_class = PersonasSerializer

##Cliente CRUD

class ClienteView(ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get(self, request, *args, **kwargs):
        clienteData = ClienteSerializer(self.get_queryset(), many=True)
        return Response(clienteData.data, status=status.HTTP_200_OK)

class ClienteViewOwner(ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get(self, request, *args, **kwargs):
        clienteData = ClienteSerializer(self.get_queryset(), many=True)
        return Response(clienteData.data, status=status.HTTP_200_OK)

class ClienteCreate(CreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def post(self, request, *args, **kwargs):
        createData = ClienteSerializer(data=request.data)
        if createData.is_valid():
            createData.save()
            return Response(createData.data, status=status.HTTP_200_OK)
        return Response(createData.errors, status=status.HTTP_400_BAD_REQUEST)

class ClienteUpdate(UpdateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDelete(DestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

##Propietario CRUD

class EmpleadoView(ListAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

    def get(self, request, *args, **kwargs):
        empleadoData = EmpleadoSerializer(self.get_queryset(), many=True)
        return Response(empleadoData.data, status=status.HTTP_200_OK)

class EmpleadoViewOwner(ListAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

    def get(self, request, *args, **kwargs):
        empleadoData = EmpleadoSerializer(self.get_queryset(), many=True)
        return Response(empleadoData.data, status=status.HTTP_200_OK)

class EmpleadoCreate(CreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

    def post(self, request, *args, **kwargs):
        createData = EmpleadoSerializer(data=request.data)
        if createData.is_valid():
            createData.save()
            return Response(createData.data, status=status.HTTP_200_OK)
        return Response(createData.errors, status=status.HTTP_400_BAD_REQUEST)

class EmpleadoUpdate(UpdateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class EmpleadoDelete(DestroyAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

