from django.urls import path
from conductoresApp.api.api import  vehiculos_asignados, vehiculos_no_asignados, asignar_conductor_vehiculo, quitar_asignacion_vehiculo

from vehiculosApp.api.api import vehiculo_api_view, vehiculo_detail_view

urlpatterns = [
    path('vehiculo/', vehiculo_api_view, name='vehiculos_api'),
    path("vehiculo/<int:pk>/", vehiculo_detail_view, name="vehiculo_detail_view"),
    path('asignados/<int:pk>/', vehiculos_asignados, name='vehiculos_asignados'),
    path('no-asignados/', vehiculos_no_asignados, name='vehiculos_no_asigandos'),
    path('asignar/', asignar_conductor_vehiculo, name='asignar'),
    path('quitar-asignacion/<int:pk>/', quitar_asignacion_vehiculo, name='quitar_asignacion'),
]
