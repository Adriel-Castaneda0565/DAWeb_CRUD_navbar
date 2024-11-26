from django.urls import path
from cliente_app import views

urlpatterns = [
    path("clientes",views.inicio_vistaClientes,name="clientes"),
    path("registrarClientes/",views.registrarClientes,name="registrarClientes"),
    path("seleccionarClientes/<id_clien>",views.seleccionarClientes,name="seleccionarClientes"),
    path("editarClientes/",views.editarClientes,name="editarClientes"),
    path("borrarClientes/<id_clien>",views.borrarClientes,name="borrarClientes"),
]