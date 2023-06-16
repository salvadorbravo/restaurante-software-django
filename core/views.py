from django.shortcuts import render, redirect
from django.views import View
from .models import Cliente, Plato

# Create your views here.

# Vista de la Lista de Platillos
class VistaPlatillos(View):
    def get(self, request):
        # veganos = Plato.objects.filter(categoria='V')
        destacados = Plato.objects.filter(categoria='D')
        # novedades = Plato.objects.filter(categoria='N')
        # generales = Plato.objects.filter(categoria='G')
        # return render(request, 'core/inicio.html', {'veganos':veganos, 'destacados':destacados, 'novedades':novedades, 'generales':generales})
        return render(request, 'core/inicio.html', {'destacados':destacados})

# Vista del Detalle del Plato
class VistaDetallePlato(View):
    def get(self, request, pk):
        plato = Plato.objects.get(pk=pk)
        return render(request, 'core/detalle-producto.html', {'plato':plato})
    
# Vista de la comida rapida
def comida_rapida(request, data=None):
    if data == None:
        rapida = Plato.objects.filter(categoria='CR')
    return render(request, 'core/comida-rapida.html', {'rapida':rapida})
   
# Vista de la comida vegana
def comida_vegana(request, data=None):
    if data == None:
        veganos = Plato.objects.filter(categoria='V')
    return render(request, 'core/comida-vegana.html', {'veganos':veganos})

# Vista de la comida casera
def comida_casera(request, data=None):
    if data == None:
        caseras = Plato.objects.filter(categoria='PC')
    return render(request, 'core/comida-casera.html', {'caseras':caseras})