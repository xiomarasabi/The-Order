from django.db import models
from apps.pedido.models import Pedido
from apps.producto.models import Producto
from apps.pedido.models import Pedido

# Create your models here.
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='detalles', on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.PositiveIntegerField()
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.cantidad} - {self.producto.nombre}"