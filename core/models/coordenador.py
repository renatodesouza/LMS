from django.db import models
from .my_user_admin import MyUserAdmin
from .user_manager import get_file_path
from stdimage import StdImageField
from datetime import date




class Coordenador(models.Model):
    
    celular = models.CharField(max_length=20)
    rc = models.IntegerField(default=0)
    usuario = models.ForeignKey(MyUserAdmin, on_delete=models.PROTECT, related_name='coordenador_usuario')
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumbnail': {'width': 480, 'height': 480, 'crop': True}})
    data_expiracao = models.DateField('Data de Expiracao', default=date(year=1900, month=1, day=1))

    class Meta:
        verbose_name = 'Coordenador'
        verbose_name_plural = 'Coordenadores'

    def __str__(self):
        return self.usuario.first_name
