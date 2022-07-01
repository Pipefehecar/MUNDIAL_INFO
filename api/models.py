from django.db import models
from .model_choices import EQUIPOS_ADMITIDOS, POSICIONES_DE_JUEGO, ROLES_ADMINISTRATIVOS
# Create your models here.
class Equipo(models.Model):
    """
    Modelo para equipos.
    """
    nombre = models.CharField(max_length=14, choices=EQUIPOS_ADMITIDOS, unique=True)#los equipos clasificados al mundial son un listado selecto, usamos choices
    bandera_img = models.CharField(max_length=350, blank=True, null=True)
    escudo_img = models.CharField(max_length=350,  blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'equipo'
        
    def __str__(self):
        return self.nombre.capitalize() 
    
    
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
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='jugadores')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['nombre', 'apellido','equipo_id']
        db_table = 'jugador'
        verbose_name_plural = 'jugadores'
    def __str__(self):
        return self.nombre.capitalize()   
    

class Directivo(models.Model):
    """
    Modelo para cuerpo tecnico.
    """
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=30)
    rol = models.CharField(max_length=3, choices=ROLES_ADMINISTRATIVOS)
    equipo_id = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'directivo'
        
    def __str__(self):
        return self.nombre.capitalize() 