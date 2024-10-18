from rest_framework.viewsets import ModelViewSet
from apps.facturacion.models import Factura
from apps.facturacion.api.serializers import FacturaSerializer
from apps.facturacion.api.permissions import IsAdminOrReadOnly

class FacturaModelViewset(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class= FacturaSerializer
    queryset = Factura.objects.all()