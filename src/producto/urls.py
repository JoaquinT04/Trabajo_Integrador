from django.urls import path
from .views import (
    listar_productos,
		detalle_producto,
		borrar_producto,)

app_name = "productos"

urlpatterns = [
    path('',listar_productos,name="listar_productos"),
    path('<int:pk>',detalle_producto,name="detalle_producto"),
    path('borrar/<int:pk>',borrar_producto,name="borrar_producto"),
]
