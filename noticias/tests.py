import datetime

from django.contrib.auth.models import Group, User
from django.test import TestCase
from django.urls import reverse

from .models import Noticia


class PortalNoticiasTests(TestCase):
    def setUp(self):
        Noticia.objects.create(titulo='Noticia vieja', fecha_ocurrencia=datetime.date(2025, 1, 1),
                               lugar='Cali', descripcion='Antigua')
        Noticia.objects.create(titulo='Noticia nueva', fecha_ocurrencia=datetime.date(2026, 11, 1),
                               lugar='Palmira', descripcion='Reciente')

    def test_portal_publico_muestra_noticias_en_orden(self):
        r = self.client.get(reverse('inicio'))
        self.assertEqual(r.status_code, 200)
        html = r.content.decode()
        self.assertLess(html.index('Noticia nueva'), html.index('Noticia vieja'))

    def test_grupo_redactores_tiene_los_4_permisos(self):
        grupo = Group.objects.get(name='Redactores')
        codigos = set(grupo.permissions.values_list('codename', flat=True))
        self.assertEqual(codigos, {'add_noticia', 'change_noticia', 'delete_noticia', 'view_noticia'})

    def test_redactor_puede_entrar_al_admin_de_noticias(self):
        u = User.objects.create_user('redactor', password='ClaveSegura123*', is_staff=True)
        u.groups.add(Group.objects.get(name='Redactores'))
        self.client.login(username='redactor', password='ClaveSegura123*')
        r = self.client.get(reverse('admin:noticias_noticia_changelist') + '?q=nueva')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Noticia nueva')
        # pero no puede gestionar usuarios
        self.assertEqual(self.client.get(reverse('admin:auth_user_changelist')).status_code, 403)
