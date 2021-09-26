from django.db import models
from .coordenador import Coordenador
from .turma import Turma
from .professor import Professor
from .curso import Curso
from .disciplina import Disciplina





class DisciplinaOfertada(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    coordenador = models.ForeignKey(Coordenador, on_delete=models.PROTECT)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    dt_inicio = models.DateField()
    dt_fim = models.DateField()
    ano = models.IntegerField()
    semestre = models.IntegerField()
    metodologia = models.TextField(max_length=255)
    recursos = models.TextField(max_length=255)
    criterio_avaliacao = models.TextField(max_length=1000)
    plano_aula = models.TextField(max_length=1000)
    

    class Meta:
        unique_together = ('curso', 'disciplina', 'turma', 'ano', 'semestre')
        verbose_name_plural = 'Disciplinas Ofertadas'

    def __str__(self):
        return self.disciplina.nome