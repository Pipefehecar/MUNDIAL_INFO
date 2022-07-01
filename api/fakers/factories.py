import factory
import factory.fuzzy
# from .model_choices import EQUIPOS_ADMITIDOS
from .models import Equipo

# EQUIPOS_ADMITIDOS = ['ALEMANIA','ARABIA SAUDITA','ARGENTINA','AUSTRALIA','BÉLGICA','BRASIL','CAMERÚN','CANADÁ','COSTA RICA','COREA DEL SUR','CROACIA','DINAMARCA','ECUADOR','ESPAÑA','ESTADOS UNIDOS','FRANCIA','GALES','GHANA','INGLATERRA','IRÁN','JAPÓN','MARRUECOS','MÉXICO','PAISES BAJOS','POLONIA','PORTUGAL','QATAR','SUIZA','SENEGAL','SERBIA','TUNEZ','URUGUAY']

class EquipoFactory(factory.django.DjangoModelFactory):
    nombre = factory.fuzzy.FuzzyChoice(choices=['ALEMANIA','ARABIA SAUDITA','ARGENTINA'])
    # bandera_img = factory.Faker("image_url")
    # escudo_img = factory.Faker("image_url")
    
    class Meta: 
        model = Equipo
        
        