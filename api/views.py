from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.models import Equipo, Jugador, Directivo
from api.serializers import EquipoSerializer, JugadorSerializer, DirectivoSerializer

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
        equipo = get_object_or_404(Equipo, id=pk)
        serializer = EquipoSerializer(instance=equipo, data=request.data, partial= True)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        equipo = get_object_or_404(Equipo, id=pk)
        equipo.delete()
        return Response(status=status.HTTP_202_ACCEPTED,data='Equipo eliminado Exitosamente')
    
    
class JugadorViewSet(ViewSet):
    """
    Endpoint para el modelo equipo.
    """
    
    def create(self, request):
        serializer = JugadorSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        jugador = Jugador.objects.all()
        serializer = JugadorSerializer(jugador, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        jugador = get_object_or_404(Jugador, pk=pk)
        serializer = JugadorSerializer(jugador)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        jugador = get_object_or_404(Jugador, id=pk)
        serializer = JugadorSerializer(instance=jugador, data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        jugador = get_object_or_404(Jugador, id=pk)
        serializer = JugadorSerializer(instance=jugador, data=request.data, partial= True)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        jugador = get_object_or_404(Jugador, id=pk)
        jugador.delete()
        return Response(status=status.HTTP_202_ACCEPTED,data='Jugador eliminado correctamente')
    
    
class DirectivoViewSet(ViewSet):
    """
    Endpoint para el modelo equipo.
    """
    
    def create(self, request):
        serializer = DirectivoSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        directivo = Directivo.objects.all()
        serializer = DirectivoSerializer(directivo, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        directivo = get_object_or_404(Directivo, pk=pk)
        serializer = DirectivoSerializer(directivo)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        directivo = get_object_or_404(Directivo, id=pk)
        serializer = DirectivoSerializer(instance=directivo, data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        directivo = get_object_or_404(Directivo, id=pk)
        serializer = DirectivoSerializer(instance=directivo, data=request.data, partial= True)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        directivo = get_object_or_404(Directivo, id=pk)
        directivo.delete()
        return Response(status=status.HTTP_202_ACCEPTED,data='Directivo eliminado correctamente')
    
    
    
