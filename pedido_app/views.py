from django.shortcuts import render,redirect
from .models import Pedido
# Create your views here.
def inicio_vistaPedidos(request):
    lospedidos = Pedido.objects.all()
    return render(request, 'gestionarPedidos.html', {'mispedidos': lospedidos})

def registrarPedidos(request):
    id_ped=request.POST["txtid_ped"]
    id_clien=request.POST["txtid_clien"]
    id_emp=request.POST["txtid_emp"]
    id_prod=request.POST["txtid_prod"]
    estado=request.POST["txtestado"]
    total=request.POST["txttotal"]
    metodo_pago=request.POST["txtmetodo_p"]
    guardarpedido=Pedido.objects.create(id_ped=id_ped,id_clien=id_clien,id_emp=id_emp,id_prod=id_prod,estado=estado,total=total,metodo_pago=metodo_pago)
    return redirect('pedidos')

def seleccionarPedidos(request,id_ped):
    Ped=Pedido.objects.get(id_ped=id_ped)
    return render(request,"editarPedidos.html",{'mispedidos':Ped})

def editarPedidos(request):
    id_ped=request.POST["txtid_ped"]
    id_clien=request.POST["txtid_clien"]
    id_emp=request.POST["txtid_emp"]
    id_prod=request.POST["txtid_prod"]
    estado=request.POST["txtestado"]
    total=request.POST["txttotal"]
    metodo_pago=request.POST["txtmetodo_p"]
    Ped=Pedido.objects.get(id_ped=id_ped)
    Ped.id_ped=id_ped
    Ped.id_clien=id_clien
    Ped.id_emp=id_emp
    Ped.id_prod=id_prod
    Ped.estado=estado
    Ped.total=total
    Ped.metodo_pago=metodo_pago

    Ped.save()
    return redirect('pedidos')

def borrarPedidos(request,id_ped):
    Ped=Pedido.objects.get(id_ped=id_ped)
    Ped.delete()
    return redirect('pedidos')