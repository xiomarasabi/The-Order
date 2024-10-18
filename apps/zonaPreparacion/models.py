from django.db import models
from apps.pedido.models import Pedido
from apps.producto.models import Producto
from apps.detalle.models import Detalle

# Create your models here.
class ZonaPreparacion(models.Model):
    
    estado= [
      ('En espera', 'En espera'),
      ('Terminado', 'Terminado') ]
    
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.ForeignKey(Detalle, on_delete=models.SET_NULL, null=True)
    estado = models.CharField(max_length=50, choices=estado, default='En espera')

    def __str__(self):
        return f"pedido:{self.pedido.nombre}, producto:{self.producto.nombre}, cantidad:{self.cantidad.cantidad}, Para llevar: {self.pedido.option}, estado:{self.estado}"