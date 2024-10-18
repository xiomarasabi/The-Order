from rest_framework.viewsets import ModelViewSet
from apps.detalle.models import DetallePedido
from apps.detalle.api.serializers import DetallePedidoSerializer

class DetallesModelViewset(ModelViewSet):
    serializer_class= DetallePedidoSerializer
    