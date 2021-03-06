# Generated by Django 2.1.3 on 2018-11-12 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0007_auto_20181112_0111'),
    ]

    operations = [
        migrations.AddField(
            model_name='disponibilidade',
            name='dia_semana',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Disponibilidade_dia_semana', to='grades.Turno'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='disponibilidade',
            name='turno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Disponibilidade_turno', to='grades.Turno'),
        ),
    ]
