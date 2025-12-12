# E-commerce - Django

**Remover venv:** ``Remove-Item -Recurse -Force venv``

## Inserção de imagens

- Instalar biblioteca ***Pillow***: ``python -m pip install Pillow``
- No arquivo ***models.py***, fazer a modelagem com ***ImageField(upload_to='', null=True, blank=True)***
- No arquivo ***settings.py*** adicionar as variaveis ***MEDIA_URL = '/media/'*** e ***MEDIA_ROOT = BASE_DIR.joinpath('media')***
- No arquivo ***urls.py*** realizar os imports: ***from django.conf.urls.static import static*** e ***from django.conf import settings***
- No mesmo arquivo, adicionar ao urlpatterns (+=) ***static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)*** e ***static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)***

Criação de admin
python manage.py createsuperuser
geovanni@teste.com
teste123

Efetuar após modelagem de app

python manage.py makemigrations # Usar após cada mudança no db
python manage.py migrate

como usar o requirements.py?

Template:

{% extends 'base.html' %}
{% block contente %}
{% endblock contente %}

a diferença entre MEDIA_ROOT e MEDIA_URL