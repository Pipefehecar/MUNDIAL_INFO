from rest_framework.serializers import ModelSerializer
from api.models import Equipo, Jugador, Directivo

class EquipoSerializer(ModelSerializer):
    class Meta:
        model = Equipo
        fields = ['id','nombre','bandera_img','escudo_img']


class JugadorSerializer(ModelSerializer):
    class Meta:
        model = Jugador
        fields = '__all__'

class JugadorCortoSerializer(ModelSerializer):
    class Meta:
        model = Jugador
        fields = ['foto','nombre','apellido','fecha_nacimiento','numero_camiseta','es_titular', 'posicion', 'equipo']

        
class DirectivoSerializer(ModelSerializer):
    class Meta:
        model = Directivo
        fields = '__all__'