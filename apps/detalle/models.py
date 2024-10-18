from django.db import models
from apps.pedido.models import Pedido
from apps.producto.models import Producto


# Create your models here.
class Detalle(models.Model):
   
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.PositiveIntegerField()
    pedido = models.ForeignKey(Pedido, related_name='detalles', on_delete=models.SET_NULL, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.cantidad} - {self.producto.nombre}"