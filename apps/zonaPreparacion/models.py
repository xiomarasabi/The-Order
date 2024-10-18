from django.db import models
from apps.pedido.models import Pedido
from apps.producto.models import Producto
from apps.detalle.models import DetallePedido

# Create your models here.
class ZonaPreparacion(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.ForeignKey(DetallePedido, on_delete=models.SET_NULL, null=True)
    estado = models.CharField(max_length=20, choices=[
        ('En espera', 'En espera'),
        ('En preparación', 'En preparación'),
        ('Terminado', 'Terminado')
    ], default='En preparación')

    def __str__(self):
        return f"pedido:{self.pedido.nombre}, producto:{self.producto.nombre}, cantidad:{self.cantidad.cantidad}, Para llevar: {self.pedido.option}, estado:{self.estado}"

# Create your models here.
