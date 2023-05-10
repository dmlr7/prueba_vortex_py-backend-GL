from pedidosApp.models import Pedido
from rest_framework import serializers

class PedidoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Pedido
        fields = ('id', 'tipo', 'direccion', 'conductor_id')
