from django.db import models
from .my_user_admin import MyUserAdmin



class Photo(models.Model):
    photo = models.ImageField('foto', upload_to='')
    usuario = models.ForeignKey(MyUserAdmin,
    on_delete=models.CASCADE, 
    related_name='photos')

    class Meta:
        ordering = ('pk',)
        verbose_name = 'foto'
        verbose_name_plural = 'fotos'

    def __str__(self):
        return str(self.user)