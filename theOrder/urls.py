"""
URL configuration for theOrder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.pedido.api.router import router_pedido
from apps.producto.api.router import router_producto
from apps.detalle.api.router import router_detalles
from apps.facturacion.api.router import router_factura
from apps.zonaPreparacion.api.router import router_preparacion

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/pedido/', include(router_pedido.urls)),
    path('api/producto/', include(router_producto.urls)),
    path('api/detalle/', include(router_detalles.urls)),
    path('api/factura/', include(router_factura.urls)),
    path('api/preparacion/', include(router_preparacion.urls)),
    
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

