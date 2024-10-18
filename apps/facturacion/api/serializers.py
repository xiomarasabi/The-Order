from rest_framework.serializers import ModelSerializer
from apps.facturacion.models import Factura

class FacturaSerializer(ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'