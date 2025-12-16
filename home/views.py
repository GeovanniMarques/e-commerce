from django.shortcuts import render, get_object_or_404
# Também poderia ser: from django.http import HttpResponse
from produtos.models import Produto # 1. Importe do modelo

# Create your views here.
def home(request):
    # 2. Busca dos produtos no banco de dados
    termo_busca = request.GET.get('busca')

    if termo_busca:
        produtos = Produto.objects.filter(nome__icontains=termo_busca)
    else:
        produtos = Produto.objects.all()

    contexto = {
        'produtos' : produtos, # 3. Exibimos a lista
    }
    
    return render(request, 'index.html', contexto) # O render pega o pedido, junta com o template e devolve a página)

def detalhe_produto(request, id):
    produto = get_object_or_404(Produto, id=id) # Busca o produto pelo ID ou retorna erro 404

    contexto = {
        'produto' : produto
    }

    return render(request, 'detalhe_produto.html', contexto)

def sobre(request):
    return render(request, 'sobre.html')