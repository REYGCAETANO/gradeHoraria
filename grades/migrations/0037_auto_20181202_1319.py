# Generated by Django 2.1.3 on 2018-12-02 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0036_auto_20181129_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dias',
            name='qtd_aulas_dia',
            field=models.IntegerField(blank=True, null=True, verbose_name='qtd'),
        ),
        migrations.AlterField(
            model_name='disponibilidade',
            name='turno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disponibilidade_turno', to='grades.Turno'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='disciplinas',
            field=models.ManyToManyField(related_name='professor_disciplina', to='grades.Disciplina', verbose_name='Disciplina'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='turnos',
            field=models.ManyToManyField(related_name='professor_turno', to='grades.Turno', verbose_name='Turno'),
        ),
        migrations.AlterField(
            model_name='semestre',
            name='aula_semana',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semestre_dias', to='grades.Dias', verbose_name='Dia da semana'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='cd_disciplinas',
            field=models.ManyToManyField(to='grades.Disciplina', verbose_name='Disciplinas'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='cd_professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turma_professor', to='grades.Professor', verbose_name='Professor'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='ds_turma',
            field=models.CharField(max_length=20, unique=True, verbose_name='Nome'),
        ),
    ]