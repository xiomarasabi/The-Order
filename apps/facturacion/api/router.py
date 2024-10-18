from rest_framework.routers import DefaultRouter
from apps.facturacion.api.views import FacturaModelViewset

router_factura = DefaultRouter()
router_factura.register(prefix="facturacion",basename="facturacion",viewset=FacturaModelViewset)