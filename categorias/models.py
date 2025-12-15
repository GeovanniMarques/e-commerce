from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=80, blank=False, null=False)
    descricao = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.nome