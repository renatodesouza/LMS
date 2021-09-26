import uuid
from django.db import models
from datetime import date
from .user_manager import UserManager
from django.contrib.auth.models import AbstractUser



class MyUserAdmin(AbstractUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    dt_expiracao = models.DateTimeField('Data de Expiracao', default=date(year=1900, month=1, day=1))
    is_staff = models.BooleanField('Menbro da equipe', default=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'dt_expiracao']

    def __str__(self):
        return self.email

    objects = UserManager()