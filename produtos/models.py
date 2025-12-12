from django.db import models

# Create your models here.
class Produto(models.Model):
    # Campo adicionado automaticamente:
    # id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=9, decimal_places=2)
    descricao = models.TextField()
    # chave_estrangeira = models.ForeignKey(nome_classe, on_delete=models.CASCADE)
    # on_delete é uma regra de segurança para o db:
    # models.CASCADE = deleta todos registros atrelados a classe estrangeira
    # models.PROTECT = bloqueia e dá erro: "Não posso apagar isso porque existem produtos dependendo dessa categoria"
    foto = models.ImageField(upload_to='produtos_fotos', blank=True, null=True)
    # upload_to='produtos_fotos': O Django criará essa pasta automaticamente para organizar as imagens
    # Status de ativo e inativo????

    # Pesquisar sobre mais nuances de modelagem, como "blank" e "choices"

    # Subclasse Produto herda métodos de Superclasse Model, como
    # .save()
    # .delete()
    # .objects.all()

    # Sempre que alguém precisar mostrar esse objeto como texto (string), por favor, mostre o conteúdo do campo nome
    def __str__(self):
        """
        Returns a string representation of the object, which is the content of the 'nome' field.
        """
        return self.nome