from django.db import models

# Create your models here.
class Proveedores(models.Model):
    id_prov=models.CharField(primary_key=True,max_length=50)
    nombre=models.CharField(max_length=30)
    ubicacion=models.CharField(max_length=30)
    telefono=models.CharField(max_length=20)
    hora=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre