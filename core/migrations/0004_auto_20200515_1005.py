# Generated by Django 3.0.5 on 2020-05-15 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200515_0954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disciplina',
            name='coordenador',
        ),
        migrations.RemoveField(
            model_name='solicitacaomatricula',
            name='turma',
        ),
    ]
