from rest_framework.serializers import ModelSerializer
from apps.detalle.models import Detalle

class DetalleSerializer(ModelSerializer):
    class Meta:
        model = Detalle
        fields = ['id','producto', 'cantidad', 'pedido','observaciones'  ]