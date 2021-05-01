from django.contrib.auth.models import Permission
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from core.models import Aluno


content_type = ContentType.objects.get_for_model(Aluno)
permission = Permission.objects.create(
    codename = 'aluno_permission',
    name = 'Aluno permission acess',
    content_type = content_type,
)
    


