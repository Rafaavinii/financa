from django.db import models
from usuario.models import Usuario

CATEGORIAS_CHOICES = (
    ('alimentacao', 'Alimentação'),
    ('moradia', 'Moradia'),
    ('educacao', 'Educação'),
    ('lazer', 'Lazer'),
    ('saude', 'Saude'),
    ('viagem', 'Viagem'),
    ('entreterimento', 'Entreterimento'),
    ('roupas', 'Roupas'),
    ('cartao', 'Cartão'),
    ('outro', 'Outro'),
    # Adicione outras categorias conforme necessário
)

class Despesa(models.Model):
    valor = models.FloatField(null=False)
    data = models.DateField(null=False)
    categoria = models.CharField(null=False, max_length=50, choices=CATEGORIAS_CHOICES)
    descricao = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
