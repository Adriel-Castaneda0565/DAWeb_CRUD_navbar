from django.urls import path
from pedido_app import views

urlpatterns = [
    path("pedidos",views.inicio_vistaPedidos,name="pedidos"),
    path("registrarPedidos/",views.registrarPedidos,name="registrarPedidos"),
    path("seleccionarPedidos/<id_ped>",views.seleccionarPedidos,name="seleccionarPedidos"),
    path("editarPedidos/",views.editarPedidos,name="editarPedidos"),
    path("borrarPedidos/<id_ped>",views.borrarPedidos,name="borrarPedidos"),
]