from django.db import models
from conductoresApp.models import Conductor


class Pedido(models.Model):
    id = models.IntegerField(primary_key=True, max_length=6)
    tipo_pedido = models.CharField('Tipo', max_length=20)
    direccion = models.CharField('Direccion', max_length=50, null=False)
    conductor_id = models.ForeignKey(
        Conductor, related_name='pedido_conductor_id', on_delete=models.CASCADE, null=False, blank=True, default="")

class Meta:

    verbose_name = 'Pedido'
    verbose_name_prural = 'Pedidos'

    def __str__(self):
        return self.id
