from rest_framework import routers
from django.urls import path, include
from .viewset import Region_ViewSet,Comuna_ViewSet,User_ViewSet,Delivery_ViewSet,Cliente_ViewSet,Restaurante_ViewSet,Direcciones_ViewSet,Producto_ViewSet,Medio_Pago_ViewSet,Pedido_ViewSet,Detalle_Pago_ViewSet,Detalle_Pedido_ViewSet,Facturado_ViewSet,Facturacion_mensual_ViewSet

router = routers.DefaultRouter()

router.register('api/region', Region_ViewSet , 'region')
router.register('api/comuna', Comuna_ViewSet , 'comuna')
router.register('api/user', User_ViewSet , 'user')
router.register('api/delivery', Delivery_ViewSet , 'delivery')
router.register('api/cliente', Cliente_ViewSet , 'cliente')
router.register('api/restaurante', Restaurante_ViewSet , 'restaurante')
router.register('api/direcciones', Direcciones_ViewSet , 'direcciones')
router.register('api/producto', Producto_ViewSet , 'producto')
router.register('api/medio_Pago', Medio_Pago_ViewSet , 'medio_Pago')
router.register('api/pedido', Pedido_ViewSet , 'pedido')
router.register('api/detalle_Pago', Detalle_Pago_ViewSet , 'detalle_Pago')
router.register('api/detalle_Pedido', Detalle_Pedido_ViewSet , 'detalle_Pedido')
router.register('api/facturado', Facturado_ViewSet , 'facturado')
router.register('api/facturacion_mensual', Facturacion_mensual_ViewSet , 'facturacion_mensual')

urlpatterns = router.urls