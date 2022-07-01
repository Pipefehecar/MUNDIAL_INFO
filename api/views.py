from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
from api.models import Equipo, Jugador, Directivo
from api.serializers import EquipoSerializer, EquipoCortoSerializer, JugadorSerializer, DirectivoSerializer, DirectivoCortoSerializer, JugadorCortoSerializer

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
        
        if equipo:
            serializer = EquipoSerializer(equipo, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':'¡Primero debe crear equipos!'})

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
        if jugador:
            serializer = JugadorSerializer(jugador, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':'¡Primero debe crear jugadores!'})
        
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
        if directivo:
            serializer = DirectivoSerializer(directivo, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':'¡Primero debe crear directivos!'})
        
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
    
    
class MundialInfoApiView(APIView):
    def get(self, request):
        num_equipos = Equipo.objects.all().count(),
        num_jugadores = Jugador.objects.all().count(),
        num_directivos = Directivo.objects.count(),
        
        
        if  num_jugadores or  num_equipos  or  num_directivos:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'pocos datos':f'equipos: {num_equipos[0]}, jugadores: {num_jugadores[0]}, directivos: {num_directivos[0]}'})
            # return Response(status=status.HTTP_400_BAD_REQUEST, data={'pocos datos': num_jugadores[0] })
            
        else:
            response = {
                'EQUIPOS_REGISTRADOS':num_equipos[0],
                'TOTAL_DE_JUGADORES':num_jugadores[0],
                'JUGADOR_MAS_JOVEN':JugadorCortoSerializer(Jugador.objects.mas_joven()).data,
                'JUGADOR_MAS_VIEJO':JugadorCortoSerializer(Jugador.objects.mas_viejo()).data,
                'TOTAL_DE_JUGADORES_SUPLENTES':Jugador.objects.suplentes().count(),
                'PROMEDIO_DE_SUPLENTES_POR_EQUIPO':Equipo.objects.prom_jugadores_suplentes(),
                # 'EQUIPO_MAS_CON_JUGADORES':Equipo.objects.mas_jugadores().nombre,
                'EQUIPO_MAS_CON_JUGADORES':EquipoCortoSerializer(Equipo.objects.mas_jugadores()).data,
                'EDAD_PROMEDIO_DE_LOS_JUGADORES':Jugador.objects.edad_prom(),
                'PROMEDIO_DE_JUGADORES_POR_EQUIPO':Equipo.objects.prom_jugadores(),
                'TECNICO_MAS_VIEJO':DirectivoCortoSerializer(Directivo.objects.tecnico_mas_viejo()).data,
            }
            return Response(status=status.HTTP_200_OK, data=response)    
