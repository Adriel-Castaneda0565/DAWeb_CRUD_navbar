from django.db import models

# Create your models here.
class Venta(models.Model):
    id_venta=models.CharField(primary_key=True,max_length=20)
    id_prod=models.CharField(max_length=10)
    id_emp=models.CharField(max_length=10)
    id_clien=models.CharField(max_length=10)
    
    def __str__(self):
        return self.id_venta