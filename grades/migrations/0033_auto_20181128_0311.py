# Generated by Django 2.1.3 on 2018-11-28 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0032_remove_disponibilidade_dia_semana'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='dias',
            unique_together=set(),
        ),
    ]
