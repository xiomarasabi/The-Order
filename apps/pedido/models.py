from django.db import models
from apps.producto.models import Producto

# Create your models here.
class Pedido(models.Model):
    
   # ESTADO= [
    #    ('En espera', 'En espera'),
     #   ('Terminado', 'Terminado') ]

    OPCION = [
        ('para llevar', 'Para llevra'),
        ('consumir', 'Consumir')]

    nombre = models.CharField(max_length=100)
    producto =models.ForeignKey(Producto, on_delete=models.SET_NULL, null = True)
    cantidad = models.IntegerField()
    observaciones =models.TextField(max_length=500)
   # estado = models.CharField(max_length=50, choices=ESTADO, default='En espera')
    option = models.CharField(max_length=50, choices=OPCION, default='Para Llevar')
    

    def __str__(self):
        return self.nombre


