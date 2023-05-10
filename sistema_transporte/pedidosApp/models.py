from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from conductoresApp.models import Conductor


class Pedido(models.Model):
    id = models.PositiveIntegerField(primary_key=True, validators=[
        MaxValueValidator(limit_value=999999999999, message="Identificador fuera de los limites superiores"),
        MinValueValidator(limit_value=1, message="Identificador fuera de los limites inferiores"),
    ])
    tipo_pedido = models.CharField('Tipo', max_length=20)
    direccion = models.CharField('Direccion', max_length=50, null=False)
    conductor_id = models.ForeignKey(
        Conductor, related_name='pedido_conductor_id', on_delete=models.CASCADE, null=False, blank=True, default="")

class Meta:

    verbose_name = 'Pedido'
    verbose_name_prural = 'Pedidos'

    def __str__(self):
        return self.id
