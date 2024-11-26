from django.db import models

# Create your models here.
class Clientes(models.Model):
    id_clien=models.CharField(primary_key=True,max_length=20)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    celular=models.CharField(max_length=30)
    direccion=models.CharField(max_length=40)
    fecha_nac=models.DateField(null=False,blank=False)
    email=models.CharField(max_length=60)
    
    def __str__(self):
        return self.nombre