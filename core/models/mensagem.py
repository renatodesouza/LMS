from django.db import models
from .aluno import Aluno
from .professor import Professor



class Mensagem(models.Model):
    ENVIADO = 'EN'
    LIDO = 'LI'
    RESPONDIDO = 'RE'

    escolha_status = [(ENVIADO, 'Enviado'), (LIDO, 'Lido'), (RESPONDIDO, 'Respondido')]

    assunto = models.TextField(max_length=255)
    referencia = models.TextField(max_length=255)
    conteudo = models.TextField(max_length=255)
    status = models.CharField(max_length=3, choices=escolha_status)
    dt_envio = models.DateField()
    dt_resposta = models.DateField()
    resposta = models.TextField(max_length=1000)
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Mensagens'

    def __str__(self):
        return self.assunto