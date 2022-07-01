from rest_framework.serializers import ModelSerializer
from api.models import Equipo, Jugador, Directivo

class EquipoSerializer(ModelSerializer):
    class Meta:
        model = Equipo
        fields = ['id','nombre','bandera_img','escudo_img', 'n_jugadores']

class EquipoCortoSerializer(ModelSerializer):
    class Meta:
        model = Equipo
        fields = ['nombre','bandera_img','escudo_img', 'n_jugadores']

class JugadorSerializer(ModelSerializer):
    class Meta:
        model = Jugador
        fields = '__all__'

class JugadorCortoSerializer(ModelSerializer):
    class Meta:
        model = Jugador
        fields = ['nombre_completo','edad','numero_camiseta','es_titular', 'posicion', 'equipo']

        
class DirectivoSerializer(ModelSerializer):
    class Meta:
        model = Directivo
        fields = '__all__'
        
class DirectivoCortoSerializer(ModelSerializer):
    class Meta:
        model = Directivo
        fields = ['nombre_completo','edad','nacionalidad','rol', 'equipo']