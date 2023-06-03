from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.VistaPlatillos.as_view(), name='inicio')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)