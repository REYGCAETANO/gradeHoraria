# Generated by Django 2.1.3 on 2018-11-19 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0014_auto_20181119_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dias',
            name='dia_semana',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Dia da Semana'),
        ),
    ]
