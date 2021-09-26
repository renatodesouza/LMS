from django.db import models
from .user_manager import get_file_path
from .my_user_admin import MyUserAdmin
from stdimage import StdImageField
from datetime import date



class Professor(models.Model):
    celular = models.CharField(max_length=20)
    rp = models.IntegerField()
    usuario = models.ForeignKey(MyUserAdmin, on_delete=models.PROTECT, related_name='professor_usuario')
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumbnail': {'width': 480, 'height': 480, 'crop': True}})
    data_expiracao = models.DateField('Data de Expiracao', default=date(year=1900, month=1, day=1))

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'

    def __str__(self):
        return self.usuario.first_name