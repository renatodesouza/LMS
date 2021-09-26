from django.db import models
from .aluno import Aluno
from .coordenador import Coordenador
from .curso import Curso



class SolicitacaoMatricula(models.Model):
    SOLICITADA = 'SO'
    REJEITADA = 'RE'
    APROVADA = 'AP'
    CANCELADA = 'CA'

    escolha_status = [(SOLICITADA, 'Solicitada'),
                    (REJEITADA, 'Rejeitada'),
                    (APROVADA, 'Aprovada'),
                    (CANCELADA, 'Cancelada'),]

    dt_solicitacao = models.DateField()
    status = models.CharField(max_length=4, choices=escolha_status, default=SOLICITADA)
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, default=None)
    coordenador = models.ForeignKey(Coordenador, on_delete=models.PROTECT)
    #disciplinaofertada = models.ForeignKey(DisciplinaOfertada, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name_plural = 'Solicitação de Matricula'

    def __str__(self):
        return self.status