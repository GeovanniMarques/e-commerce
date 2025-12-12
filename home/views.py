from django.shortcuts import render
# Também poderia ser: from django.http import HttpResponse
from produtos.models import Produto # 1. Importe do modelo

# Create your views here.
def home(request):
    # 2. Busca dos produtos no banco de dados
    produtos_reais = Produto.objects.all()

    contexto = {
        'nome' : 'Geovanni',
        'produtos' : produtos_reais # 3. Exibimos a lista
    }
    
    return render(request, 'index.html', contexto) # O render pega o pedido, junta com o template e devolve a página)

def sobre(request):
    return render(request, 'sobre.html')