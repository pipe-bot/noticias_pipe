"""
Configuración del proyecto portal_noticias (Django 5.2).

Funciona igual en tu computador (modo desarrollo) y en PythonAnywhere
(modo producción). En producción se definen variables de entorno en el
archivo WSGI de PythonAnywhere (ver README.md).
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# En producción se reemplaza con la variable de entorno DJANGO_SECRET_KEY.
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'django-insecure-iwnd%o%1myvo7d5dui^$+5np7(0r@9t#0%wfvkklbm_**a9&fm',
)

# En tu PC queda en True. En PythonAnywhere se pone DJANGO_DEBUG=False.
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

# Dominios desde los que se puede abrir la página.
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.pythonanywhere.com']
if DEBUG:
    ALLOWED_HOSTS = ['*']


# Aplicaciones
INSTALLED_APPS = [
    'semantic_admin',          # tema visual del panel (debe ir antes de admin)
    'semantic_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'noticias.apps.NoticiasConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portal_noticias.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,  # busca plantillas en <app>/templates/
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'portal_noticias.wsgi.application'


# Base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Idioma y zona horaria (panel en español, hora de Colombia)
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True


# Archivos estáticos (CSS, JS del admin)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'   # aquí los junta "collectstatic"

# Archivos subidos por los usuarios (imágenes de las noticias)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
