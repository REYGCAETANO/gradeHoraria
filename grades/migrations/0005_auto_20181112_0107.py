# Generated by Django 2.1.3 on 2018-11-12 03:07

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0004_auto_20181112_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='nm_disciplina',
            field=multiselectfield.db.fields.MultiSelectField(max_length=200, verbose_name='Nome da Disciplina'),
        ),
    ]