# Generated by Django 2.1.2 on 2018-11-28 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0029_auto_20181128_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disponibilidade',
            name='dia_semana',
            field=models.ManyToManyField(default='-1', related_name='Disponibilidade_dia_semana', to='grades.Dias'),
        ),
    ]
