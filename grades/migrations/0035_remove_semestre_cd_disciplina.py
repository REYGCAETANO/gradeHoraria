# Generated by Django 2.1.3 on 2018-11-28 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0034_auto_20181128_0314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semestre',
            name='cd_disciplina',
        ),
    ]
