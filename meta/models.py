from django.db import models

from usuario.models import Usuario

class Meta(models.Model):
    nome_meta = models.CharField(max_length=50)
    valor_alvo = models.FloatField()
    progresso = models.FloatField()
    concluida = models.BooleanField(default=None)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

 