from django.db import models
from .professor import Professor




class Atividade(models.Model):
    titulo = models.CharField(max_length=255, unique=True)
    descricao = models.TextField(max_length=255)
    conteudo = models.TextField(max_length=255)
    tipo = models.TextField(max_length=255)
    extras = models.TextField(max_length=255)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'

    def __str__(self):
        return self.titulo