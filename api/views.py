from api.models import Equipo
from django.shortcuts import get_object_or_404
from api.serializers import EquipoSerializer
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.
class EquipoViewSet(viewsets.ViewSet):
    """
    Endpoint para el modelo equipo.
    """
    def list(self, request):
        queryset = Equipo.objects.all()
        serializer = EquipoSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Equipo.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = EquipoSerializer(user)
        return Response(serializer.data)