
import sistema_transporte.helpers as res
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from conductoresApp.api.serializers import ConductorSerializer
from conductoresApp.models import Conductor
from rest_framework import status
from rest_framework.response import Response
from vehiculosApp.api.serializers import VehiculoSerializer
from pedidosApp.api.serializers import PedidoSerializer

from vehiculosApp.models import Vehiculo
from pedidosApp.models import Pedido
@api_view(['GET', 'POST'])
def conductor_api_view(request):

    #List users
    if request.method == 'GET':        
        conductores = Conductor.objects.all().values('id', 'nombre','apellido', 'telefono', 'identificacion', 'direccion')
        conductores_serializer = ConductorSerializer(conductores, many = True)
        return  Response(res.HttpResponse(status.HTTP_200_OK, conductores_serializer.data, 'Lista de conductores'), status= status.HTTP_200_OK)
    
    #Create user
    elif request.method == 'POST':
        conductores_serializer = ConductorSerializer(data = request.data)
        if conductores_serializer.is_valid():
            conductores_serializer.save()
            return Response(res.HttpResponse(status.HTTP_200_OK, conductores_serializer.data, 'Creación exitosa' ),status= status.HTTP_201_CREATED)
        
        return Response(res.HttpResponse( status.HTTP_400_BAD_REQUEST,  conductores_serializer.errors,  'Algo salio mal' ), status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def conductor_detail_view(request, pk):

    #Queryset (Consultar si el usuario existe)
    conductor = Conductor.objects.filter(id=pk).first()
    if conductor:

        #Find user by id
        if request.method == 'GET':
            conductor_serializer = ConductorSerializer(conductor)
            return Response(res.HttpResponse(status.HTTP_200_OK, conductor_serializer.data, 'Búsqueda exitosa' ), status=status.HTTP_200_OK)
        
        #Update user
        elif request.method == 'PUT':
            request.data
            conductor = Conductor.objects.filter(id=pk).first()
            conductor_serializer = ConductorSerializer(conductor, data = request.data)
            if conductor_serializer.is_valid():
                conductor_serializer.save()
                return Response(res.HttpResponse(status.HTTP_200_OK, conductor_serializer.data, 'Actualización exitosa' ) , status= status.HTTP_200_OK)
            return Response(res.HttpResponse(status.HTTP_400_BAD_REQUEST, conductor_serializer.errors, 'Algo salio mal' ), status = status.HTTP_400_BAD_REQUEST)
        
        #Delete user
        elif request.method == 'DELETE':
            conductor = Conductor.objects.filter(id=pk).first()
            conductor.delete()
            return Response( res.HttpResponse(status.HTTP_200_OK, {}, 'Conductor eliminado' ), status= status.HTTP_200_OK)
    return Response(res.HttpResponse(status.HTTP_400_BAD_REQUEST, {}, 'El conductor no fue encontrado' ), status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def vehiculos_asignados(request, pk):

    #Queryset (Consultar si el usuario existe)
    vehiculos = Vehiculo.objects.filter(conductor_id = pk)
    
    if vehiculos:

        #Find user by id
        if request.method == 'GET':
            vehiculos_serializer = VehiculoSerializer(vehiculos, many=True)
            return Response(res.HttpResponse(status.HTTP_200_OK, vehiculos_serializer.data, 'Vehículos asociados'),
                            status=status.HTTP_200_OK)
        
        #Update user
        elif request.method == 'PUT':
            request.data
            vehiculo = Vehiculo.objects.filter(id= request.data.get('id')).first()
            vehiculos_serializer = VehiculoSerializer(vehiculo, data = request.data)
            if vehiculos_serializer.is_valid():
                vehiculos_serializer.save()
                return Response(res.HttpResponse(status.HTTP_200_OK, vehiculos_serializer.data, 'Actualización exitosa'), status= status.HTTP_200_OK)
            return Response(res.HttpResponse(status.HTTP_400_BAD_REQUEST, vehiculos_serializer.errors, 'Algo salio mal'), status = status.HTTP_400_BAD_REQUEST)
    return Response(res.HttpResponse(status.HTTP_400_BAD_REQUEST, {}, 'No se han encontrado vehículos con estos datos'), status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def vehiculos_no_asignados(request):

    vehiculos = Vehiculo.objects.filter(conductor_id = None)
    if vehiculos:
        #Find user by id

        if request.method == 'GET':
            vehiculos_serializer = VehiculoSerializer(vehiculos, many=True)
            return Response(res.HttpResponse(status.HTTP_200_OK, vehiculos_serializer.data, ''),status=status.HTTP_200_OK)


    return Response(res.HttpResponse(status.HTTP_400_BAD_REQUEST, {}, 'No se han encontrado vehículos con estos datos'), status = status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def asignar_conductor_vehiculo(request):
    print('este es el id', request.data.get('id'))
    vehiculo = Vehiculo.objects.filter(id= request.data.get('id')).first()

    if vehiculo:

        if request.method == 'PUT':
                
                vehiculos_serializer = VehiculoSerializer(vehiculo, data = request.data)
                if vehiculos_serializer.is_valid() and vehiculo.conductor_id == None:
                    vehiculos_serializer.save()
                    return Response(res.HttpResponse(status.HTTP_200_OK, vehiculos_serializer.data, 'Asignación completa') , status= status.HTTP_200_OK)
                return Response(res.HttpResponse(status.HTTP_400_BAD_REQUEST, vehiculos_serializer.errors, 'Algo salio mal'), status = status.HTTP_400_BAD_REQUEST)
    else:
        return Response(res.HttpResponse(status.HTTP_400_BAD_REQUEST, {}, 'No se han encontrado vehículos con estos datos'), status = status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def quitar_asignacion_vehiculo(request):

    vehiculo = Vehiculo.objects.filter(id=request.data.get('id')).first()

    if vehiculo:

        if request.method == 'PUT':
                request.data
                vehiculos_serializer = VehiculoSerializer(vehiculo, data = request.data)
                if vehiculos_serializer.is_valid():
                    vehiculos_serializer.save()
                    return Response(res.HttpResponse(status.HTTP_200_OK, vehiculos_serializer.data, 'Se quita asignación'), status= status.HTTP_200_OK)
                return Response(res.HttpResponse(status.HTTP_400_BAD_REQUEST, vehiculos_serializer.errors, 'Algo salio mal'), status = status.HTTP_400_BAD_REQUEST)
    return Response(res.HttpResponse(status.HTTP_400_BAD_REQUEST, {}, 'No se han encontrado vehículos con estos datos'), status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def pedidos_asignados(request, pk):
    # Queryset (Consultar si el usuario existe)
    pedido = Pedido.objects.filter(conductor_id=pk)

    if pedido:

        # Find user by id
        if request.method == 'GET':
            pedidos_serializer = PedidoSerializer(pedido, many=True)
            return Response(res.HttpResponse(status.HTTP_200_OK, pedidos_serializer.data, 'Vehículos asociados'),
                            status=status.HTTP_200_OK)

        # Update user
        elif request.method == 'PUT':
            request.data
            pedido = Pedido.objects.filter(id=request.data.get('id')).first()
            pedidos_serializer = PedidoSerializer(pedido, data=request.data)
            if pedidos_serializer.is_valid():
                pedidos_serializer.save()
                return Response(
                    res.HttpResponse(status.HTTP_200_OK, pedidos_serializer.data, 'Actualización exitosa'),
                    status=status.HTTP_200_OK)
            return Response(
                res.HttpResponse(status.HTTP_400_BAD_REQUEST, pedidos_serializer.errors, 'Algo salio mal'),
                status=status.HTTP_400_BAD_REQUEST)
    return Response(res.HttpResponse(status.HTTP_400_BAD_REQUEST, {}, 'No se han encontrado vehículos con estos datos'),
                    status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def pedidos_no_asignados(request):
    pedidos = Vehiculo.objects.filter(conductor_id=None)
    if pedidos:
        # Find user by id

        if request.method == 'GET':
            pedidos_serializer = PedidoSerializer(pedidos, many=True)
            return Response(res.HttpResponse(status.HTTP_200_OK, pedidos_serializer.data, ''),
                            status=status.HTTP_200_OK)

    return Response(res.HttpResponse(status.HTTP_400_BAD_REQUEST, {}, 'No se han encontrado vehículos con estos datos'),
                    status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def asignar_conductor_pedido(request):
    print('este es el id', request.data.get('id'))
    pedido = Pedido.objects.filter(id=request.data.get('id')).first()

    if pedido:

        if request.method == 'PUT':

            pedidos_serializer = VehiculoSerializer(pedido, data=request.data)
            if pedidos_serializer.is_valid() and pedido.conductor_id == None:
                pedidos_serializer.save()
                return Response(res.HttpResponse(status.HTTP_200_OK, pedidos_serializer.data, 'Asignación completa'),
                                status=status.HTTP_200_OK)
            return Response(
                res.HttpResponse(status.HTTP_400_BAD_REQUEST, pedidos_serializer.errors, 'Algo salio mal'),
                status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(
            res.HttpResponse(status.HTTP_400_BAD_REQUEST, {}, 'No se han encontrado vehículos con estos datos'),
            status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def quitar_asignacion_pedido(request):
    pedido = Vehiculo.objects.filter(id=request.data.get('id')).first()

    if pedido:

        if request.method == 'PUT':
            request.data
            pedidos_serializer = PedidoSerializer(pedido, data=request.data)
            if pedidos_serializer.is_valid():
                pedidos_serializer.save()
                return Response(res.HttpResponse(status.HTTP_200_OK, pedidos_serializer.data, 'Se quita asignación'),
                                status=status.HTTP_200_OK)
            return Response(
                res.HttpResponse(status.HTTP_400_BAD_REQUEST, pedidos_serializer.errors, 'Algo salio mal'),
                status=status.HTTP_400_BAD_REQUEST)
    return Response(res.HttpResponse(status.HTTP_400_BAD_REQUEST, {}, 'No se han encontrado vehículos con estos datos'),
                    status=status.HTTP_400_BAD_REQUEST)

