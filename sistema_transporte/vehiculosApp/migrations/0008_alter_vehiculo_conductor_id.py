# Generated by Django 4.2 on 2023-04-12 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conductoresApp', '0003_alter_conductor_id'),
        ('vehiculosApp', '0007_alter_vehiculo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='conductor_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='conductor_id', to='conductoresApp.conductor'),
        ),
    ]
