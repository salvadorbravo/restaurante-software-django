from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.VistaPlatillos.as_view(), name='inicio'),
    path('detalle-producto/<int:pk>', views.VistaDetallePlato.as_view(), name='detalle-producto'),
    # Pagina de la comida rapida
    
    # Pagina de los platos Caseros
    path('comida-casera/', views.comida_casera, name="comida-casera"),
    path('comida-casera/<slug:data>', views.comida_casera, name="comida-casera"),
    # Pagina de los platos Veganos
    path('comida-vegana/', views.comida_vegana, name="comida-vegana"),
    path('comida-vegana/<slug:data>', views.comida_vegana, name="comida-vegana"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)