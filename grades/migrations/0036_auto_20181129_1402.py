# Generated by Django 2.1.3 on 2018-11-29 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0035_remove_semestre_cd_disciplina'),
    ]

    operations = [

        migrations.AlterField(
            model_name='professor',
            name='nm_professor',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),

        migrations.AlterUniqueTogether(
            name='professor',
            unique_together={('matricula',)},
        ),
    ]
