from rest_framework.routers import DefaultRouter
from apps.detalle.api.views import DetalleModelViewSet

router_detalles = DefaultRouter()
router_detalles.register(prefix="detalles",basename="detalles",viewset=DetalleModelViewSet)