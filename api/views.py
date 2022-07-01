from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.models import Equipo
from api.serializers import EquipoSerializer

# Create your views here.
class EquipoViewSet(ViewSet):
    """
    Endpoint para el modelo equipo.
    """
    
    def create(self, request):
        serializer = EquipoSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        equipo = Equipo.objects.all()
        serializer = EquipoSerializer(equipo, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        equipo = get_object_or_404(Equipo, pk=pk)
        serializer = EquipoSerializer(equipo)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        equipo = get_object_or_404(Equipo, id=pk)
        serializer = EquipoSerializer(instance=equipo, data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        equipo = get_object_or_404(Equipo.objects.all(), id=pk)
        serializer = EquipoSerializer(instance=equipo, data=request.data, partial= True)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        equipo = get_object_or_404(Equipo, id=pk)
        equipo.delete()
        return Response(status=status.HTTP_202_ACCEPTED,data='borrado con exito')