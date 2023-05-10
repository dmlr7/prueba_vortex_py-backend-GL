from django.urls import path

from conductoresApp.api.api import  pedidos_asignados, pedidos_no_asignados, asignar_conductor_vehiculo, quitar_asignacion_vehiculo

from pedidosApp.api.api import pedido_api_view, pedido_detail_view

urlpatterns = [
    path('pedido/', pedido_api_view, name='pedido_api'),
    path("pedido/<int:pk>/", pedido_detail_view, name="pedido_detail_view"),
    path('asignados/<int:pk>/', pedidos_asignados, name='pedidos_asignados'),
    path('no-asignados/', pedidos_no_asignados, name='pedidos_no_asigandos'),
    path('asignar/', asignar_conductor_vehiculo, name='asignar_conductor_pedido'),
    path('quitar-asignacion/<int:pk>/', quitar_asignacion_vehiculo, name='quitar_asignacion_pedido'),
]
