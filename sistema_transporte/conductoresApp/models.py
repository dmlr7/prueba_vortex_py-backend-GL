from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator


# Create your models here.
class Conductor(models.Model):
    
    identificacion = models.PositiveIntegerField('Identificacion', unique=True, null=False, validators=[
        MaxValueValidator(limit_value=99999999999, message="Identificador fuera de los limites superiores"),
        MinValueValidator(limit_value=1, message="Identificador fuera de los limites inferiores"),
    ])
    nombre = models.CharField('Nombre',max_length=20, unique=False, null=False)
    apellido = models.CharField('Apellido',max_length=20, unique=False, null= True)
    telefono = models. PositiveIntegerField('Telefono',unique=False, null=False, validators=[
        MaxValueValidator(limit_value=99999999999, message="Identificador fuera de los limites superiores"),
        MinValueValidator(limit_value=1, message="Identificador fuera de los limites inferiores"),
    ])
    direccion = models.CharField('Direccion',max_length=50, unique=True, null=True)

class Meta:

    verbose_name = 'Conductor'
    verbose_name_prural = 'Conductores'

    def __str__(self):
        return self.identificacion