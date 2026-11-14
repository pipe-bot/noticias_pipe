from django.contrib import admin
from django.utils.html import format_html
from semantic_admin import SemanticModelAdmin

from .models import Noticia


@admin.register(Noticia)
class NoticiaAdmin(SemanticModelAdmin):
    # Columnas visibles en el listado
    list_display = ('miniatura', 'titulo', 'fecha_ocurrencia', 'lugar')
    list_display_links = ('miniatura', 'titulo')

    # Filtros (barra lateral) y búsqueda por varios campos
    list_filter = ('fecha_ocurrencia', 'lugar')
    search_fields = ('titulo', 'lugar', 'descripcion')
    date_hierarchy = 'fecha_ocurrencia'   # navegación por año / mes / día

    ordering = ('-fecha_ocurrencia',)
    list_per_page = 10

    # Formulario de crear / editar
    fields = ('titulo', 'fecha_ocurrencia', 'lugar', 'descripcion', 'imagen', 'vista_previa')
    readonly_fields = ('vista_previa',)

    @admin.display(description='Imagen')
    def miniatura(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" style="width:70px;height:50px;object-fit:cover;border-radius:4px;">',
                obj.imagen.url,
            )
        return '—'

    @admin.display(description='Vista previa')
    def vista_previa(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" style="max-width:300px;border-radius:6px;">', obj.imagen.url)
        return 'Sin imagen'
