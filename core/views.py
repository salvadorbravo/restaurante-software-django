from django.shortcuts import render, redirect
from django.views import View
from .models import Cliente, Plato

# Create your views here.

# Vista de la Lista de Platillos
class VistaPlatillos(View):
    def get(self, request):
        veganos = Plato.objects.filter(categoria='V')
        mas_vendidos = Plato.objects.filter(categoria='MV')
        novedades = Plato.objects.filter(categoria='N')
        generales = Plato.objects.filter(categoria='G')
        return render(request, 'core/inicio.html', {'veganos':veganos, 'mas_vendidos':mas_vendidos, 'novedades':novedades, 'generales':generales})
        