from django.db import models

from usuario.models import Usuario

class Meta(models.Model):
    nome_meta = models.CharField(max_length=50)
    valor_alvo = models.FloatField()
    progresso = models.FloatField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
