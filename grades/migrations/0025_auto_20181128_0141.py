# Generated by Django 2.1.2 on 2018-11-28 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0024_auto_20181127_2349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disponibilidade',
            old_name='id_disponibilidade',
            new_name='id_indisponibilidade',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='disponibilidades',
        ),
        migrations.AddField(
            model_name='disponibilidade',
            name='professores',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='grades.Professor'),
        ),
        migrations.RemoveField(
            model_name='disponibilidade',
            name='dia_semana',
        ),
        migrations.AddField(
            model_name='disponibilidade',
            name='dia_semana',
            field=models.ManyToManyField(related_name='Disponibilidade_dia_semana', to='grades.Dias'),
        ),
    ]
