from django.db import models
from .aluno import Aluno
from .solicitacao_matricula import SolicitacaoMatricula
from .turma import Turma
from .curso import Curso



class Matricula(models.Model):
    ATIVA = 'AV'
    CANCELADA = 'CA'
    TRANCADA = 'TA'
    ANALISE = 'AE'

    escolha_situacao = [
        (ATIVA, 'Ativa'),
        (CANCELADA, 'Cancelada'),
        (TRANCADA, 'Trancada'),
        (ANALISE, 'Analise')
        ]

    dt_inicio = models.DateField()
    dt_fim = models.DateField()
    status = models.CharField(max_length=4, choices=escolha_situacao, default=ANALISE)
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, default=None)
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT, default=None)
    solicitacao_matricula = models.ForeignKey(SolicitacaoMatricula, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Matricula'
        verbose_name_plural = 'Matriculas'

    def __str__(self):
        return self.status