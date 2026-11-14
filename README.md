# Portal de Noticias - CAI SENA Valle

Proyecto del curso de Django. Es un portal donde se publican
las noticias del Centro de Automatización Industrial.

## Qué tiene
- Página pública con las noticias, de la más reciente a la más antigua
- Panel de administración para crear, editar y borrar noticias
- Búsqueda y filtros por fecha y lugar
- Grupo Redactores que solo puede manejar las noticias

## Cómo correrlo
python -m venv vnoticias
vnoticias\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Hecho con Django 5.2.19