# Generated by Django 2.1.3 on 2018-11-18 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0008_auto_20181112_0211'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='turno',
            options={'ordering': ['cd_turno'], 'verbose_name': 'Turno', 'verbose_name_plural': 'Turnos'},
        ),
        migrations.AlterField(
            model_name='turno',
            name='cd_turno',
            field=models.CharField(choices=[('1', 'Matutino'), ('2', 'Vespertino'), ('3', 'Noturno')], max_length=1, verbose_name='Turno'),
        ),
        migrations.AlterField(
            model_name='turno',
            name='dia_semana',
            field=models.CharField(choices=[('1', 'Domingo-Feira'), ('2', 'Segunda-Feira'), ('3', 'Terça-Feira'), ('4', 'Quarta-Feira'), ('5', 'Quinta-Feira'), ('6', 'Sexta-Feira'), ('7', 'Sábado')], max_length=100, verbose_name='Dia da Semana'),
        ),
    ]