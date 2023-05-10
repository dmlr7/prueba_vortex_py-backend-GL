from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from pedidosApp.api.serializers import PedidoSerializer
from pedidosApp.models import Pedido
from sistema_transporte import helpers as res

@api_view(['GET', 'POST'])
def pedido_api_view(request) -> Response:

    #List users
    if request.method == 'GET':        
        pedidos = Pedido.objects.all()
        pedidos_serializer  = PedidoSerializer(pedidos, many = True)
        return  Response(
            res.HttpResponse(
                data=pedidos_serializer.data,
                statusCode=status.HTTP_200_OK,
                message="Lista de pedidos",
            ),
            status= status.HTTP_200_OK)

    #Create user
    elif request.method == 'POST':
        pedidos_serializer = PedidoSerializer(data = request.data)
        if pedidos_serializer.is_valid():
            pedidos_serializer.save()
            return Response(
                    res.HttpResponse(
                    data=pedidos_serializer,
                    statusCode=status.HTTP_201_CREATED,
                    message="Pedido creado",
                    ),
                status= status.HTTP_201_CREATED
            )
        
        return Response(
                res.HttpResponse(
                    data=pedidos_serializer.errors,
                    statusCode=status.HTTP_400_BAD_REQUEST,
                    message="Algo salio mal",
                ),
            status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def pedido_detail_view(request, pk: int) -> Response:

    #Queryset (Consultar si el usuario existe)
    pedido = Pedido.objects.filter(id=pk).first()
    if pedido:

        #Find user by id
        if request.method == 'GET':
            pedidos_serializer = PedidoSerializer(pedido)
            return Response(pedidos_serializer.data, status=status.HTTP_200_OK)
        
        #Update user
        elif request.method == 'PUT':
            request.data
            pedido = Pedido.objects.filter(id=pk).first()
            pedidos_serializer = PedidoSerializer(pedido, data = request.data)
            if pedidos_serializer.is_valid():
                pedidos_serializer.save()
                return Response(pedidos_serializer.data , status= status.HTTP_200_OK)
            return Response(pedidos_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        #Delete user
        elif request.method == 'DELETE':
            pedido = Pedido.objects.filter(id=pk).first()
            pedido.delete()
            return Response({'message': 'Pedido eliminado correctamente!'} , status= status.HTTP_200_OK)
    return Response({'message': 'No se ha encontrado el pedido con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
