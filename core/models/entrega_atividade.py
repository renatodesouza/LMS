from django.db import models
from .atividade_vinculada import AtividadeVinculada
from .aluno import Aluno
from .professor import Professor




class EntregaAtividade(models.Model):
    ENTREGUE = 'EN'
    CORRIGIDO = 'CO'

    escolha_status = [(ENTREGUE, 'Entregue'), (CORRIGIDO, 'Corrigido')]

    titulo = models.CharField(max_length=100)
    resposta = models.TextField(max_length=255)
    dt_entrega = models.DateField()
    status = models.CharField(max_length=2, choices=escolha_status, default=ENTREGUE)
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    dt_avaliacao = models.DateField()
    obs = models.TextField(max_length=255)
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    atividade_vinculada = models.ForeignKey(AtividadeVinculada, on_delete=models.PROTECT)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    file = models.FileField(upload_to='file', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Entrega das Atividades'

    def __str__(self):
        return self.atividade_vinculada.atividade.titulo