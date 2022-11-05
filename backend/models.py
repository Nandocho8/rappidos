from django.db import models

# Create your models here.


class Region(models.Model):
    nombre_region = models.CharField(
        "Nombre region", max_length=80, blank=false, null=false)


class Comuna(models.Model):
    nombre_comuna = models.CharField(
        "Nombre comuna", max_length=80, blank=false, null=false)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


class User(AbstractUser):
    CLIENTE = 'C'
    DELIVERY = 'D'
    RESTAURANTE = 'R'

    TYPE_USER = [
        CLIENTE, 'Cliente',

        DELIVERY, 'Repartidor',
        RESTAURANTE, 'Restaurante',
    ]

    email = models.EmailField("Email", blank=False, null=False)
    password = models.CharField("Password", blank=False, null=False)
    tipo = models.CharField(
        "Tipo", max_length=1, choices=TYPE_USER, default=CLIENTE)
    is_active = models.BooleanField("Esta activo", default=True)


class Delivery(models.Model):
    rut_delivery = models.IntegerField("Rut", blank=False, null=False)
    dv_rut_delivery = models.CharField("Digito Verificador", max_length=1, choices=[
                                       0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'K'])
    nombre_delivery = models.CharField("Nombres", max_length=50)
    apellidos_delivery = models.CharField("Apellidos", max_length=50)
    usuarios = models.OneToOneField(to=User, on_delete=CASCADE)


class Cliente(models.Model):
    nombre_cliente = models.CharField("Nombres", max_length=50)
    apellidos_cliente = models.CharField("Apellidos", max_length=50)
    usuarios = models.OneToOneField(to=User, on_delete=CASCADE)


class Restaurante(models.Model):
    rut_restaurante = models.IntegerField("Rut", blank=False, null=False)
    dv_rut_restaurante = models.CharField("Digito Verificador", max_length=1, choices=[
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'K'])
    razon_social_restaurante = models.CharField("Razon Social", max_length=150)
    usuarios = models.OneToOneField(to=User, on_delete=CASCADE)
    direccion_restaurante = models.CharField(
        "Direccion empresa", max_length=60, blank=False, null=False)
    clasificacion_restaurante = models.DecimalField(
        "Clasificacion Restaurante", max_digits=3, decimal_places=2, blank=False, null=False)
    comuna = models.ForeignKey(to=Comuma, on_delete=CASCADE)


class Direcciones(models.Model):
    calle_direccion = models.CharField(
        "Direccion", max_length=60, blank=False, null=False)
    numeracion_direccion = models.IntegerField(
        "Numero direccion", blank=False, null=False)
    depto_ofic_direccion = models.CharField(
        "Depto / Oficina / Block", max_length=12, blank=False, null=False)
    cliente = models.ForeignKey(to=Cliente, on_delete=CASCADE)
    comuna = models.ForeignKey(to=Comuna, on_delete=CASCADE)


class Producto(models.Model):
    nombre_producto = models.CharField(
        "Nombre", max_length=50, blank=False, null=False)
    precio_venta_producto = models.IntegerField(
        "Precio Venta", blank=False, null=False)
    precio_costo_producto = models.IntegerField(
        "Precio Costo", blank=False, null=False)
    tiene_stock = models.BooleanField(
        "Disponible", default=True, blank=False, null=False)
    restaurante = models.ForeignKey(to=Restaurante, on_delete=CASCADE)


class Medio_Pago(models.Model):
    medio_pago = models.CharField("Medio de Pago", max_length=50,
                                  blank=False, null=False)


class Pedido(models.Model):
    estado = models.CharField("Estado", max_length=50,
                              blank=False, null=False, default='En preparación')
    restaurante = models.ForeignKey(to=Restaurante, on_delete=CASCADE)
    cliente = models.ForeignKey(to=Cliente, on_delete=CASCADE)
    delivery = models.ForeignKey(to=Delivery, on_delete=CASCADE)


class Detalle_Pago(models.Model):
    pedido = models.ForeignKey(to=Pedido, on_delete=CASCADE)
    num_transaccion = models.IntegerField(
        "Numero de transaccion", max_length=80, blank=False, null=False)
    monto_total_pedido = models.IntegerField(
        "Total Pedido", max_length=6, blank=False, null=False)
    medio_pago = models.ForeignKey(to=Medio_Pago, on_delete=CASCADE)


class Detalle_Pedido(models.Model):
    pedido = models.ForeignKey(to=Pedido, on_delete=CASCADE)
    producto = models.ForeignKey(to=Producto, on_delete=CASCADE)


class Facturado(models.Model):
    numero_facura = models.IntegerField(
        "Numero Factura", max_length=12, blank=False, null=False)
    monto_neto_factura = models.IntegerField(
        "Neto Factura", max_length=12, blank=False, null=False)
    monto_bruto_factura = models.IntegerField(
        "Bruto Factura", max_length=12, blank=False, null=False)
    inicio_periodo_facturacion = models.DateField(
        "Inicio periodo facturacion", auto_now_add=True, blank=False, null=False)
    termino_periodo_facturacion = models.DateField(
        "Termino periodo facturacion", auto_now_add=True, blank=False, null=False)
    fecha_pago = models.DateField(
        "Fecha de pago", auto_now_add=True, blank=False, null=False)
    usuarios = models.OneToOneField(to=User, on_delete=CASCADE)

class Facturacion_mensual(models.Model):
    id_usuario = models.IntegerField("Id usuario", blank=False, null=False)
    tipo_usuario = models.CharField(
        "Tipo Usuario", max_length=1, blank=False, null=False, choices=['R','D','A'])
    id_pedido = models.IntegerField("Id pedido", blank=False, null=False)
    fecha_transaccion = models.DateField(
        "Fecha transaccion", auto_now_add=True, blank=False, null=False)
    monto_facturado = models.IntegerField(
        "Monto Facturado",  blank=False, null=False)
