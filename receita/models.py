from django.db import models

from usuario.models import Usuario

CATEGORIAS_CHOICES = (
    ('salario', 'Salário'),
    ('investimento', 'Investimento'),
    ('renda', 'Renda'),
    ('presente', 'Presente'),
    ('outros', 'Outros'),
)

class Receita(models.Model):
    valor = models.FloatField()
    categoria = models.CharField(null=False, max_length=50, choices=CATEGORIAS_CHOICES)
    descricao = models.CharField(max_length=500)
    data = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
