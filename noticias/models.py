from django.db import models


class Noticia(models.Model):
    titulo = models.CharField('Título', max_length=200)
    fecha_ocurrencia = models.DateField('Fecha en que ocurrió')
    lugar = models.CharField('Lugar', max_length=200)
    descripcion = models.TextField('Descripción')
    imagen = models.ImageField('Imagen', upload_to='noticias/', blank=True, null=True)

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'
        ordering = ['-fecha_ocurrencia', '-id']   # la más reciente primero

    def __str__(self):
        return self.titulo
