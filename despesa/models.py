from django.db import models
from usuario.models import Usuario

CATEGORIAS_CHOICES = (
    ('alimentacao', 'Alimentação'),
    ('moradia', 'Moradia'),
    ('educacao', 'Educação'),
    ('lazer', 'Lazer'),
    ('saude', 'Saude'),
    ('outro', 'Outro'),
    # Adicione outras categorias conforme necessário
)

class Despesa(models.Model):
    valor = models.FloatField()
    data = models.DateField()
    categoria = models.CharField(max_length=50, choices=CATEGORIAS_CHOICES)
    descricao = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
