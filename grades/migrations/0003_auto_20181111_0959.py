# Generated by Django 2.1.3 on 2018-11-11 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0002_auto_20181111_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='disponibilidades',
            field=models.ManyToManyField(blank=True, to='grades.Disponibilidade', verbose_name='Disponibilidades'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='nm_professor',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='professor',
            name='turno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grades.Turno', verbose_name='Turno'),
        ),
        migrations.AlterField(
            model_name='semestre',
            name='cd_turno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grades.Turno', verbose_name='Turno'),
        ),
    ]