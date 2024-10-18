from rest_framework.viewsets import ViewSet
from rest_framework.viewsets import ModelViewSet
from apps.producto.models import Producto
from apps.producto.api.serializers import ProductoSerializer
from apps.producto.api.permissions import IsAdminOrReadOnly


class ProductoViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()
    http_method_names = ['get','put']