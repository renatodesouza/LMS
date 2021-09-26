from django.db import models
from .my_user_admin import MyUserAdmin
from stdimage import StdImageField, JPEGField


class Disciplina(models.Model):
    ABERTO = 'AB'
    FECHADO = 'FC'

    escolha_status = [(ABERTO, 'Aberto'), (FECHADO, 'Fechado')]

    nome = models.CharField(max_length=255, unique=True)
    data = models.DateField()
    status = models.CharField(max_length=2, choices=escolha_status, default=ABERTO)   
    plano_ensino = models.TextField(max_length=5000)
    carga_horaria = models.IntegerField()
    competencias = models.TextField(max_length=1000)
    habilidades = models.TextField(max_length=1000)
    ementa = models.TextField(max_length=5000)
    Conteudo_programatico = models.TextField(max_length=5000)
    bibliografia_basica = models.TextField(max_length=1000)
    bibliografia_complementar = models.TextField(max_length=1000)
    percentual_pratico = models.DecimalField(max_digits=13, decimal_places=2)
    percentual_teorico = models.DecimalField(max_digits=13, decimal_places=2)

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'

    def __str__(self):
        return self.nome