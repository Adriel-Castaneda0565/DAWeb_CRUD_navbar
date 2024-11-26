from django.urls import path
from empleados_app import views

urlpatterns = [
    path("empleado",views.inicio_vistaEmpleado,name="empleado"),
    path("registrarEmpleados/",views.registrarEmpleados,name="registrarEmpleados"),
    path("seleccionarEmpleados/<ide>",views.seleccionarEmpleados,name="seleccionarEmpleados"),
    path("editarEmpleados/",views.editarEmpleados,name="editarEmpleados"),
    path("borrarEmpleados/<ide>",views.borrarEmpleados,name="borrarEmpleados"),
]
