# Generated by Django 4.2.5 on 2023-09-25 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudiante',
            old_name='pais_origen_id',
            new_name='curso',
        ),
    ]
