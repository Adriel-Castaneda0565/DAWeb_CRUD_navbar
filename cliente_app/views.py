from django.shortcuts import render,redirect
from .models import Clientes
# Create your views here.

def inicio_vistaClientes(request):
    losclientes=Clientes.objects.all()

    return render(request,"gestionarClientes.html",{'misclientes':losclientes})

def registrarClientes(request):
    id_clien=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    celular=request.POST["txtcel"]
    direccion=request.POST["txtdir"]
    fecha_nac=request.POST["txtfe"]
    email=request.POST["txtemail"]
    guardarclientes=Clientes.objects.create(id_clien=id_clien,nombre=nombre,apellido=apellido,celular=celular,direccion=direccion,fecha_nac=fecha_nac,email=email)
    return redirect('clientes')

def seleccionarClientes(request,id_clien):
    Cliente=Clientes.objects.get(id_clien=id_clien)
    return render(request,"editarClientes.html",{'misclientes':Cliente})

def editarClientes(request):
    id_clien=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    celular=request.POST["txtcel"]
    direccion=request.POST["txtdir"]
    fecha_nac=request.POST["txtfe"]
    email=request.POST["txtemail"]
    Cliente=Clientes.objects.get(id_clien=id_clien)
    Cliente.nombre=nombre
    Cliente.apellido=apellido
    Cliente.celular=celular
    Cliente.direccion=direccion
    Cliente.fecha_nac=fecha_nac
    Cliente.email=email
    
    Cliente.save()
    return redirect('clientes')

def borrarClientes(request,id_clien):
    Cliente=Clientes.objects.get(id_clien=id_clien)
    Cliente.delete()
    return redirect('clientes')