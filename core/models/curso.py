from django.db import models
from .user_manager import get_file_path
from .coordenador import Coordenador
from stdimage import StdImageField


class Curso(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(max_length=2000, default=None)
    destaque = models.CharField(max_length=255, default=None)
    mercado_trabalho = models.TextField(max_length=1000)
    coordenador = models.ForeignKey(Coordenador, on_delete=models.CASCADE, default=None)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumbnail': {'width': 1500, 'height': 500, 'crop': True}})
    imagem2 = StdImageField('Imagem dois', upload_to=get_file_path, variations={'thumbnail': {'width': 480, 'height': 480, 'crop': True}})
    
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.nome