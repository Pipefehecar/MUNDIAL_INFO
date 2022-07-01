from rest_framework.routers import DefaultRouter
from api.views import EquipoViewSet, JugadorViewSet, DirectivoViewSet

router_equipo = DefaultRouter()
router_equipo.register(prefix='equipos', basename='equipos', viewset=EquipoViewSet)

router_jugador = DefaultRouter()
router_jugador.register(prefix='jugadores', basename='jugadores', viewset=JugadorViewSet)

router_directivo = DefaultRouter()
router_directivo.register(prefix='directivos', basename='directivos', viewset=DirectivoViewSet)