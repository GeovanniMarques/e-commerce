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

<!-- {% comment %}
    <h2>Produtos em Destaque:</h2>
    <ul>
        {% for produto in produtos %}
        <li>{{ produto.nome }} - R${{ produto.preco }} - <strong>Descrição: </strong> {{ produto.descricao }}</li>
        {% if produto.foto %}
        <li><img src="{{ produto.foto.url }}" alt="Foto de {{ produto.nome }}" width="150px"></li>
        {% else %}
        <li><img src="../media/produto-sem-imagem.gif" alt="Produto sem imagem" width="150px"></li>
        {% endif %}
        {% endfor %}
    </ul>
    {% endcomment %} -->

## Templates:

card e card-body: Criam a caixa branca bonita.

card-img-top: Faz a imagem encaixar perfeitamente no topo do cartão.

style="object-fit: cover;": Isso é um truque de CSS inline para garantir que todas as fotos fiquem do mesmo tamanho, sem esticar ou amassar, mesmo que você tenha feito upload de fotos de tamanhos diferentes.

truncatewords:20: Um filtro do Django que corta o texto se a descrição for muito longa, para não quebrar o layout.