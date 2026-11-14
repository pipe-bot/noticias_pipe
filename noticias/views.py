from django.shortcuts import render

from .models import Noticia


def lista_noticias(request):
    """Página pública: todas las noticias, de la más reciente a la más antigua."""
    noticias = Noticia.objects.order_by('-fecha_ocurrencia', '-id')
    return render(request, 'noticias/lista.html', {'noticias': noticias})
