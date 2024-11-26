from django.shortcuts import render,redirect
from .models import Proveedores
# Create your views here.

def inicio_vistaProveedores(request):
    losproveedores=Proveedores.objects.all()

    return render(request,"gestionarProveedores.html",{'misproveedores':losproveedores})

def registrarProveedores(request):
    id_prov=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    ubicacion=request.POST["txtubi"]
    telefono=request.POST["txttel"]
    hora=request.POST["txthora"]
    email=request.POST["txtemail"]
    guardarproveedores=Proveedores.objects.create(id_prov=id_prov,nombre=nombre,ubicacion=ubicacion,telefono=telefono,hora=hora,email=email)
    return redirect('proveedores')

def seleccionarProveedores(request,id_prov):
    Prov=Proveedores.objects.get(id_prov=id_prov)
    return render(request,"editarProveedores.html",{'misproveedores':Prov})

def editarProveedores(request):
    id_prov=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    ubicacion=request.POST["txtubi"]
    telefono=request.POST["txttel"]
    hora=request.POST["txthora"]
    email=request.POST["txtemail"]
    Prov=Proveedores.objects.get(id_prov=id_prov)
    Prov.nombre=nombre
    Prov.ubicacion=ubicacion
    Prov.telefono=telefono
    Prov.hora=hora
    Prov.email=email
    
    Prov.save()
    return redirect('proveedores')

def borrarProveedores(request,id_prov):
    Prov=Proveedores.objects.get(id_prov=id_prov)
    Prov.delete()
    return redirect('proveedores')