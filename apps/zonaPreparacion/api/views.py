from rest_framework.viewsets import ModelViewSet
from apps.zonaPreparacion.models import ZonaPreparacion
from apps.zonaPreparacion.api.serializers import zonaPreparacionSerializer

class zonaPreparacionModelViewSet(ModelViewSet):
    serializer_class= zonaPreparacionSerializer
    queryset = ZonaPreparacion.objects.all()