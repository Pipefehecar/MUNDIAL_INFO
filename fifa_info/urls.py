"""
    fifa_info URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from api.views import MundialInfoApiView
from api.router import router_equipo, router_jugador, router_directivo
from django.views.generic import RedirectView
#documentacion
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Copa Mundial FIFA 2022: API de informacion de los equipos",
      default_version='v1',
      description="Esta api lista informacion de los directivos, jugadores y equipos pertenecientes al campeonato mundial Qatar 2022",
      terms_of_service="https://digitalhub.fifa.com/m/3e8de757aac56c6b/original/dc7szy6nllfz06qgz2ry-pdf.pdf",
      contact=openapi.Contact(email="luisherrerac@yahoo.com",),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
#    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', RedirectView.as_view(permanent=False, url='/api/docs/')),
    path('admin/', admin.site.urls),
    path('api/', include(router_equipo.urls)),
    path('api/', include(router_jugador.urls)),
    path('api/', include(router_directivo.urls)),
    path('api/mundial-info/', MundialInfoApiView.as_view()),
    
    #enpoints de documentacion
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
