# Generated by Django 2.1.2 on 2018-11-28 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0020_auto_20181125_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='disciplina',
            field=models.ManyToManyField(related_name='professor_disciplina', to='grades.Disciplina'),
        ),
    ]
