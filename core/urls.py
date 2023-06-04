from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.VistaPlatillos.as_view(), name='inicio'),
    path('detalle-producto/<int:pk>', views.VistaDetallePlato.as_view(), name='detalle-producto'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)