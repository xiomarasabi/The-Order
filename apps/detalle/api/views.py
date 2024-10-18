from rest_framework.viewsets import ViewSet
from rest_framework.viewsets import ModelViewSet
from apps.detalle.models import Detalle
from apps.detalle.api.serializers import DetalleSerializer
from apps.detalle.api.permissions import IsAdminOrReadOnly



class DetalleModelViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = DetalleSerializer
    queryset = Detalle.objects.all()
    