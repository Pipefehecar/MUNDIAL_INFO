from django.db import models
from datetime import date
from django.db.models import Avg, Max, Min, F, Count, Q
from django.db.models.functions import Extract
from .model_choices import EQUIPOS_ADMITIDOS, POSICIONES_DE_JUEGO, ROLES_ADMINISTRATIVOS
# Create your models here.

class EquipoManager(models.Manager):
    def prom_jugadores(self):
        return self.all().annotate(num_jugad = Count('jugadores')).aggregate(prom_jugad=Avg('num_jugad')).get('prom_jugad')
       
    def prom_jugadores_suplentes(self):
        return self.all().annotate(num_jugad = Count('jugadores', filter=Q(jugadores__es_titular=False))).aggregate(prom_jugad=Avg('num_jugad')).get('prom_jugad')
             
    def mas_jugadores(self):
        return self.all().annotate(num_jugad = Count('jugadores')).order_by('-num_jugad').first()
        
        
class Equipo(models.Model):
    """
    Modelo para equipos.
    """
    nombre = models.CharField(max_length=30, unique=True)#los equipos clasificados al mundial son un listado selecto, usamos choices
    bandera_img = models.CharField(max_length=350, blank=True, null=True)
    escudo_img = models.CharField(max_length=350,  blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = EquipoManager()
    
   
    class Meta:
        db_table = 'equipo'
        
    def __str__(self):
        return self.nombre.capitalize() 

    @property
    def n_jugadores(self):
        return Jugador.objects.filter(equipo_id=self.id).count()
    
class JugadorManager(models.Manager):
    def suplentes(self):
        return super().get_queryset().filter(es_titular=False)
    
    def titulares(self):
        return super().get_queryset().filter(es_titular=True)
    
    def mas_viejo(self):
        return super().get_queryset().order_by('fecha_nacimiento')[0]
        
    def mas_joven(self):
        return super().get_queryset().order_by('-fecha_nacimiento')[0]
    
    def edad_prom(self):
        return self.annotate(edad=(date.today().year - Extract('fecha_nacimiento', 'year'))).aggregate(prom_edad=Avg('edad')).get('prom_edad')
   
        
class Jugador(models.Model):
    """
    Modelo para jugadores.
    """
    foto = models.CharField(max_length=350, blank=True, null=True)
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    fecha_nacimiento = models.DateField()
    numero_camiseta = models.PositiveIntegerField()
    es_titular = models.BooleanField(default=True)
    posicion = models.CharField(max_length=3, choices=POSICIONES_DE_JUEGO)
    equipo_id = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='jugadores')
    created_at = models.DateTimeField(auto_now_add=True)
    objects = JugadorManager()
   
    class Meta:
        unique_together = ['nombre', 'apellido','equipo_id']
        db_table = 'jugador'
        verbose_name_plural = 'jugadores'
        
    def __str__(self):
        return self.nombre.capitalize()
    
    @property
    def equipo(self):
        return self.equipo_id.nombre
    
    @property
    def edad(self) -> int:
        return date.today().year - self.fecha_nacimiento.year
    
    @property
    def nombre_completo(self):
        return f'{self.nombre} {self.apellido}'   


class DirectivoManager(models.Manager):
    def tecnico_mas_viejo(self):
        return super().get_queryset().filter(rol='TEC').order_by('fecha_nacimiento')[0]
              

class Directivo(models.Model):
    """
    Modelo para cuerpo tecnico.
    """
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=30)
    rol = models.CharField(max_length=3, choices=ROLES_ADMINISTRATIVOS)
    equipo_id = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='directivos')
    created_at = models.DateTimeField(auto_now_add=True)
    objects = DirectivoManager()
    
    class Meta:
        db_table = 'directivo'
        
    def __str__(self):
        return self.nombre.capitalize() 
    
    @property
    def equipo(self):
        return self.equipo_id.nombre
    
    @property
    def edad(self) -> int:
        return date.today().year - self.fecha_nacimiento.year
    
    @property
    def nombre_completo(self):
        return f'{self.nombre} {self.apellido}' 