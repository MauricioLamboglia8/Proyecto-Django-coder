# Generated by Django 4.1.2 on 2022-11-08 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appcoder', '0002_entregable_estudiante_profesor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entregable',
            old_name='fechaDeEntrega',
            new_name='fecha_de_entrega',
        ),
    ]
