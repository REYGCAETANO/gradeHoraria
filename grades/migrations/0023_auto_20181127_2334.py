# Generated by Django 2.1.2 on 2018-11-28 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0022_auto_20181127_2324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='turno',
        ),
        migrations.AddField(
            model_name='professor',
            name='turnos',
            field=models.ManyToManyField(related_name='professor_turno', to='grades.Turno'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='matricula',
            field=models.CharField(max_length=50, verbose_name='Matrícula'),
        ),
    ]
