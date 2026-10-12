from django.contrib import admin
from django.urls import path, include # Agregamos include aquí

# dos líneas nuevas que ya estaban en mis proyectos anteriores
from django.conf import settings
from django.conf.urls.static import static

# sugerencia de chatGPT
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('libreria.urls')), # Conectamos las rutas de la librería
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

