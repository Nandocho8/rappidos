from rest_framework import viewsets, permissions
from .models import Region, Comuna, User, Delivery, Cliente, Restaurante, Direcciones, Producto, Medio_Pago, Pedido, Detalle_Pago, Detalle_Pedido, Facturado, Facturacion_mensual
from .serializers import Region_Serializers, Comuna_Serializers, User_Serializers, Delivery_Serializers, Cliente_Serializers, Restaurante_Serializers, Direcciones_Serializers, Producto_Serializers, Medio_Pago_Serializers, Pedido_Serializers, Detalle_Pago_Serializers, Detalle_Pedido_Serializers, Facturado_Serializers, Facturacion_mensual_Serializers
from rappidos import settings
from django_filters.rest_framework import DjangoFilterBackend


class Region_ViewSet(viewsets.ModelViewSet):

    queryset = Region.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Region_Serializers
    #filter_backends [DjangoFilterBackend]
    #filterset_fields = ['algo']


class Comuna_ViewSet(viewsets.ModelViewSet):

    queryset = Comuna.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Comuna_Serializers
    #filter_backends [DjangoFilterBackend]
    #filterset_fields = ['algo']


class User_ViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = User_Serializers
    #filter_backends [DjangoFilterBackend]
    #filterset_fields = ['algo']


class Delivery_ViewSet(viewsets.ModelViewSet):

    queryset = Delivery.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Delivery_Serializers
    #filter_backends [DjangoFilterBackend]
    #filterset_fields = ['algo']


class Cliente_ViewSet(viewsets.ModelViewSet):

    queryset = Cliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Cliente_Serializers
    #filter_backends [DjangoFilterBackend]
    #filterset_fields = ['algo']


class Restaurante_ViewSet(viewsets.ModelViewSet):

    queryset = Restaurante.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Restaurante_Serializers
    #filter_backends [DjangoFilterBackend]
    #filterset_fields = ['algo']


class Direcciones_ViewSet(viewsets.ModelViewSet):

    queryset = Direcciones.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Direcciones_Serializers
    #filter_backends [DjangoFilterBackend]
    #filterset_fields = ['algo']


class Producto_ViewSet(viewsets.ModelViewSet):

    queryset = Producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Producto_Serializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['restaurante__id']


class Medio_Pago_ViewSet(viewsets.ModelViewSet):

    queryset = Medio_Pago.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Medio_Pago_Serializers
    #filter_backends [DjangoFilterBackend]
    #filterset_fields = ['algo']


class Pedido_ViewSet(viewsets.ModelViewSet):

    queryset = Pedido.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Pedido_Serializers
    #filter_backends [DjangoFilterBackend]
    #filterset_fields = ['algo']


class Detalle_Pago_ViewSet(viewsets.ModelViewSet):

    queryset = Detalle_Pago.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Detalle_Pago_Serializers
    #filter_backends [DjangoFilterBackend]
    #filterset_fields = ['algo']


class Detalle_Pedido_ViewSet(viewsets.ModelViewSet):

    queryset = Detalle_Pedido.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Detalle_Pedido_Serializers
    #filter_backends [DjangoFilterBackend]
    #filterset_fields = ['algo']


class Facturado_ViewSet(viewsets.ModelViewSet):

    queryset = Facturado.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Facturado_Serializers
    #filter_backends [DjangoFilterBackend]
    #filterset_fields = ['algo']


class Facturacion_mensual_ViewSet(viewsets.ModelViewSet):

    queryset = Facturacion_mensual.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Facturacion_mensual_Serializers
    #filter_backends [DjangoFilterBackend]
    #filterset_fields = ['algo']
