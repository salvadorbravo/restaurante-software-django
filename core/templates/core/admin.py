from django.contrib import admin
from .models import Cliente, Plato

# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'nombre', 'localidad', 'ciudad', 'codigo_postal', 'region']
    
@admin.register(Plato)
class PlatoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'precio_venta', 'descripcion', 'categoria', 'imagen_producto']