# Generated by Django 4.2 on 2023-04-12 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculosApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='capacidad',
            field=models.CharField(max_length=7, verbose_name='Capacidad'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='placa',
            field=models.CharField(max_length=7, verbose_name='Placa'),
        ),
    ]
