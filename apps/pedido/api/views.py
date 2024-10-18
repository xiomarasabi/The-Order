from rest_framework.viewsets import ViewSet
from rest_framework.viewsets import ModelViewSet
from apps.pedido.models import Pedido
from apps.pedido.api.serializers import PedidoSerializer
from apps.pedido.api.permissions import IsAdminOrReadOnly


class PedidoViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all()