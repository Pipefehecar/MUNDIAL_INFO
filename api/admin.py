from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'created_at']
    
@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'posicion', 'es_titular', 'equipo_id']
    
@admin.register(Directivo)
class DirectivoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido','rol', 'equipo_id']