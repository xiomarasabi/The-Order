from rest_framework.viewsets import ModelViewSet
from apps.facturacion.models import Factura
from apps.facturacion.api.serializers import FacturaSerializer

class FacturaModelViewset(ModelViewSet):
    serializer_class= FacturaSerializer
    queryset = Factura.objects.all()