from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from noticias.views import lista_noticias

# Textos del encabezado del panel administrativo
admin.site.site_header = 'Portal de Noticias · CAI SENA Valle'
admin.site.site_title = 'Administración de noticias'
admin.site.index_title = 'Panel de administración'

urlpatterns = [
    path('', lista_noticias, name='inicio'),
    path('admin/', admin.site.urls),
]

# En desarrollo Django sirve las imágenes subidas.
# En PythonAnywhere las sirve el servidor (sección "Static files" del Web tab).
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
