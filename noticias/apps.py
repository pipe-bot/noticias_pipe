from django.apps import AppConfig
from django.db.models.signals import post_migrate


def crear_grupo_redactores(sender, **kwargs):
    """Crea (o actualiza) el grupo 'Redactores' con los 4 permisos de Noticia.

    Se ejecuta solo cada vez que se corre `python manage.py migrate`, así el
    grupo existe también en PythonAnywhere sin tener que crearlo a mano.
    """
    from django.contrib.auth.models import Group, Permission

    grupo, _ = Group.objects.get_or_create(name='Redactores')
    permisos = Permission.objects.filter(
        content_type__app_label='noticias',
        codename__in=['add_noticia', 'change_noticia', 'delete_noticia', 'view_noticia'],
    )
    grupo.permissions.add(*permisos)


class NoticiasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'noticias'
    verbose_name = 'Portal de noticias'

    def ready(self):
        post_migrate.connect(crear_grupo_redactores, sender=self)
