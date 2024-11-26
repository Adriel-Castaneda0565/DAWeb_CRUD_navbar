from django.shortcuts import render,redirect
from .models import Venta
# Create your views here.

def inicio_vistaVenta(request):
    lasventas=Venta.objects.all()

    return render(request,"gestionarVentas.html",{'misventas':lasventas})

def registrarVentas(request):
    id_venta=request.POST["txtid"]
    id_prod=request.POST["txtid_prod"]
    id_emp=request.POST["txtid_emp"]
    id_clien=request.POST["txtid_clien"]
    guardarventa=Venta.objects.create(id_venta=id_venta,id_prod=id_prod,id_emp=id_emp,id_clien=id_clien)
    return redirect('venta')

def seleccionarVentas(request,id_venta):
    vent=Venta.objects.get(id_venta=id_venta)
    return render(request,"editarVentas.html",{'misventas':vent})

def editarVentas(request):
    id_venta=request.POST["txtid"]
    id_prod=request.POST["txtid_prod"]
    id_emp=request.POST["txtid_emp"]
    id_clien=request.POST["txtid_clien"]
    vent=Venta.objects.get(id_venta=id_venta)
    vent.id_prod=id_prod
    vent.id_emp=id_emp
    vent.id_clien=id_clien
    
    vent.save()
    return redirect('venta')

def borrarVentas(request,id_venta):
    vent=Venta.objects.get(id_venta=id_venta)
    vent.delete()
    return redirect('venta')