from django.db import models
from datetime import date
from .professor import Professor
from .disciplina_ofertada import DisciplinaOfertada
from .atividade import Atividade



class AtividadeVinculada(models.Model):
    ABERTA = 'ABERTA'
    FECHADA = 'FECHADA'
    PRORROGADA = 'PRORROGADA'
    
    AC1 = 'AC1'
    AC2 = 'AC2'
    AC3 = 'AC3'
    AC4 = 'AC4'
    AC5 = 'AC5'
    AC6 = 'AC6'
    AC7 = 'AC7'
    AC8 = 'AC8'
    AC9 = 'AC9'
    AC10 = 'AC10'

    escolha_status = [
                    (ABERTA, 'Aberta'),
                    (FECHADA, 'Fechada'),
                    (PRORROGADA, 'Prorrogada'),]
    
    escolha_atividade = [(AC1, 'AC1'),
                         (AC2, 'AC2'),
                         (AC3, 'AC3'),
                         (AC4, 'AC4'),
                         (AC5, 'AC5'),
                         (AC6, 'AC6'),
                         (AC7, 'AC7'),
                         (AC8,  'AC8'),
                         (AC9, 'AC9'),
                         (AC10, 'AC10')]

    status = models.CharField(max_length=15, choices=escolha_status)
    atividade_vinculada = models.CharField('Atividade Complementar', max_length=4, choices=escolha_atividade, default=AC1)
    rotulo = models.CharField(max_length=255)
    dt_inicio = models.DateField('Data Inicio', default=date(year=1900, month=1, day=1))
    dt_fim = models.DateField('Data Fim', default=date(year=1900, month=1, day=1))
    atividade = models.ForeignKey(Atividade, on_delete=models.PROTECT)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    disciplina_ofertada = models.ForeignKey(DisciplinaOfertada, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Atividades Vinculadas'

    def __str__(self):
        return self.rotulo