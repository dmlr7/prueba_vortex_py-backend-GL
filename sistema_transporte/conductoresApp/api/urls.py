from django.urls import path
from conductoresApp.api.api import conductor_api_view, conductor_detail_view, vehiculos_asignados, vehiculos_no_asignados

urlpatterns = [
    path('conductor/', conductor_api_view, name='conductores_api'),
    path("conductor/<int:pk>/", conductor_detail_view, name="Conductor_detail_view"),
    path('vehiculos_asignados/<int:pk>/', vehiculos_asignados, name='vehiculos_asignados'),
    path('vehiculos_no_asignados/<int:pk>/', vehiculos_no_asignados, name='vehiculos_no_asigandos'),
    path('pedidos_asignados/<int:pk>/', vehiculos_asignados, name='vehiculos_asignados'),
    path('pedidos_no_asignados/<int:pk>/', vehiculos_no_asignados, name='vehiculos_no_asigandos'),

]
