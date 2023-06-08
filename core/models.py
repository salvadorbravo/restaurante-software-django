from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.

# Modelo de Cliente
REGION_CHOISES = (
    ("I	Región de Tarapacá", "I	Región de Tarapacá"),
    ("II Región de Antofagasta", "II Región de Antofagasta"),
    ("III Región de Atacama", "III Región de Atacama"),
    ("IV Región de Coquimbo", "IV Región de Coquimbo"),
    ("V Región de Valparaíso", "V Región de Valparaíso"),
    ("VI Región del Libertador General Bernardo OHiggins", "VI Región del Libertador General Bernardo OHiggins"),
    ("VII Región del Maule", "VII Región del Maule"),
    ("VIII Región del Bio-bío", "VIII Región del Bio-bío"),
    ("IX Región de La Araucanía", "IX Región de La Araucanía"),
    ("X Región de Los Lagos", "X Región de Los Lagos"),
    ("XI Región Aysén del General Carlos Ibáñez del Campo", "XI Región Aysén del General Carlos Ibáñez del Campo"),
    ("XII Región de Magallanes y Antártica Chilena", "XII Región de Magallanes y Antártica Chilena"),
    ("Región Metropolitana de Santiago", "Región Metropolitana de Santiago"),
    ("XIV Región de Los Ríos", "XIV Región de Los Ríos"),
    ("XV Región de Arica y Parinacota", "XV Región de Arica y Parinacota"),
    ("XVI Región de Ñuble", "XVI Región de Ñuble")
)

class Cliente(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    localidad = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    codigo_postal = models.IntegerField()
    region = models.CharField(choices=REGION_CHOISES, max_length=200)
    
    class Meta:
        verbose_name_plural = 'Cliente'
        
    def __str__(self):
        return self(self.id)
    
# Modelo del Plato
CATEGORIA_CHOISES = (
    ("V", "Veganos"),
    ("MV", "Mas Vendidos"),
    ("N", "Novedades"),
    ("G", "Generales")
)

class Plato(models.Model):
    nombre = models.CharField(max_length=200)
    precio_venta = models.FloatField(validators=[MinValueValidator(1.0)])
    descripcion = models.TextField()
    categoria = models.CharField(choices=CATEGORIA_CHOISES, max_length=80)
    imagen_producto = models.ImageField(upload_to='imagenproducto')
    
    class Meta:
        verbose_name_plural = 'Platillo'
        
    def __str__(self):
        return str(self.id)