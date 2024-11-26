from django.db import models

# Create your models here.
class Pedido(models.Model):
    id_ped=models.CharField(primary_key=True,max_length=10)
    id_clien=id_clien=models.CharField(max_length=10)
    id_emp = models.CharField(max_length=10)
    id_prod = models.CharField(max_length=10)
    estado = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    def __str__(self):
        return self.id_ped