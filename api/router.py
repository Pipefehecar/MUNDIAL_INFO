from rest_framework.routers import DefaultRouter
from api.views import EquipoViewSet

router_equipo = DefaultRouter()
router_equipo.register(prefix='equipos', basename='equipos', viewset=EquipoViewSet)

