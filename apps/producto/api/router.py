from rest_framework.routers import DefaultRouter
from apps.producto.api.views import ProductoViewSet
router_producto = DefaultRouter()
router_producto.register(prefix="producto", basename="producto", viewset= ProductoViewSet)