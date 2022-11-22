from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Region(models.Model):
    nombre_region = models.CharField(
        "Nombre region", max_length=80, blank=False, null=False)

    def __str__(self):
        return self.nombre_region


class Comuna(models.Model):
    nombre_comuna = models.CharField(
        "Nombre comuna", max_length=80, blank=False, null=False)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_comuna


class User(AbstractUser):
    CLIENTE = 'C'
    DELIVERY = 'D'
    RESTAURANTE = 'R'

    TYPE_USER = [
        (CLIENTE, 'Cliente'),

        (DELIVERY, 'Repartidor'),
        (RESTAURANTE, 'Restaurante'),
    ]

    email = models.EmailField("email", blank=False, null=False, unique=True)
    password = models.CharField(
        "Password", max_length=250, blank=False, null=False)
    tipo = models.CharField(
        "Tipo", max_length=1, choices=TYPE_USER, default=CLIENTE)
    is_active = models.BooleanField("Esta activo", default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.tipo} {self.email}'


class Delivery(models.Model):
    rut_delivery = models.IntegerField("Rut", blank=False, null=False)
    dv_rut_delivery = models.CharField("Digito Verificador", max_length=1)
    nombre_delivery = models.CharField("Nombres", max_length=50)
    apellidos_delivery = models.CharField("Apellidos", max_length=50)
    usuarios = models.OneToOneField(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre_delivery} {self.apellidos_delivery}'


class Cliente(models.Model):
    nombre_cliente = models.CharField("Nombres", max_length=50)
    apellidos_cliente = models.CharField("Apellidos", max_length=50)
    usuarios = models.OneToOneField('User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre_cliente} {self.apellidos_cliente}'


class Restaurante(models.Model):
    rut_restaurante = models.IntegerField("Rut", blank=False, null=False)
    dv_rut_restaurante = models.CharField("Digito Verificador", max_length=1)
    razon_social_restaurante = models.CharField("Razon Social", max_length=150)
    nombre_fantasia_restaurante = models.CharField(
        "Nombre Fantasia", max_length=55)
    usuarios = models.OneToOneField(to=User, on_delete=models.CASCADE)
    direccion_restaurante = models.CharField(
        "Direccion empresa", max_length=60, blank=False, null=False)
    tipo_restaurante = models.CharField(
        "Tipo Restaurante", max_length=60, blank=False, null=False)

    clasificacion_restaurante = models.DecimalField(
        "Clasificacion Restaurante", max_digits=2, decimal_places=1, blank=False, null=False)
    comuna = models.ForeignKey(to=Comuna, on_delete=models.CASCADE)
    imagen_restaurante = models.CharField(
        "Imagen", max_length=2000, default='https://cdn.dribbble.com/users/708069/screenshots/8550972/media/4b5777eeb628444504852dc56a67367d.png?compress=1&resize=768x576&vertical=top')

    def __str__(self):
        return self.razon_social_restaurante


class Direcciones(models.Model):
    calle_direccion = models.CharField(
        "Direccion", max_length=60, blank=False, null=False)
    numeracion_direccion = models.IntegerField(
        "Numero direccion", blank=False, null=False)
    depto_ofic_direccion = models.CharField(
        "Depto / Oficina / Block", max_length=12, blank=False, null=False)
    cliente = models.ForeignKey(to=Cliente, on_delete=models.CASCADE)
    comuna = models.ForeignKey(to=Comuna, on_delete=models.CASCADE)

    def __str__(self):
        direccion = f'{self.calle_direccion} {self.numeracion_direccion}'
        if self.numeracion_direccion != NULL:
            direccion += f' {self.numeracion_direccion}'
        return direccion


class Producto(models.Model):
    nombre_producto = models.CharField(
        "Nombre", max_length=200, blank=False, null=False)
    precio_venta_producto = models.IntegerField(
        "Precio Venta", blank=False, null=False)
    precio_costo_producto = models.IntegerField(
        "Precio Costo", blank=False, null=False)
    tiene_stock = models.BooleanField(
        "Disponible", default=True, blank=False, null=False)
    descripcion_producto = models.CharField(
        "Detalle Producto", max_length=2000, blank=False, null=False)
    restaurante = models.ForeignKey(to=Restaurante, on_delete=models.CASCADE)

    imagen_producto = models.CharField(
        "Imagen", max_length=2000, default='https://cdn.dribbble.com/users/708069/screenshots/8550972/media/4b5777eeb628444504852dc56a67367d.png?compress=1&resize=768x576&vertical=top')

    def __str__(self):
        return self.nombre_producto


class Medio_Pago(models.Model):
    medio_pago = models.CharField("Medio de Pago", max_length=50,
                                  blank=False, null=False)

    def __str__(self):
        return self.medio_pago


class Pedido(models.Model):
    estado = models.CharField("Estado", max_length=50,
                              blank=False, null=False, default='En preparación')
    restaurante = models.ForeignKey(to=Restaurante, on_delete=models.CASCADE)
    cliente = models.ForeignKey(to=Cliente, on_delete=models.CASCADE)
    delivery = models.ForeignKey(to=Delivery, on_delete=models.CASCADE)


class Detalle_Pago(models.Model):
    pedido = models.ForeignKey(to=Pedido, on_delete=models.CASCADE)
    num_transaccion = models.IntegerField(
        "Numero de transaccion", blank=False, null=False)
    monto_total_pedido = models.IntegerField(
        "Total Pedido", blank=False, null=False)
    medio_pago = models.ForeignKey(to=Medio_Pago, on_delete=models.CASCADE)


class Detalle_Pedido(models.Model):
    pedido = models.ForeignKey(to=Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(to=Producto, on_delete=models.CASCADE)


class Facturado(models.Model):
    numero_facura = models.IntegerField(
        "Numero Factura",  blank=False, null=False)
    monto_neto_factura = models.IntegerField(
        "Neto Factura",  blank=False, null=False)
    monto_bruto_factura = models.IntegerField(
        "Bruto Factura",  blank=False, null=False)
    inicio_periodo_facturacion = models.DateField(
        "Inicio periodo facturacion", auto_now_add=True, blank=False, null=False)
    termino_periodo_facturacion = models.DateField(
        "Termino periodo facturacion", auto_now_add=True, blank=False, null=False)
    fecha_pago = models.DateField(
        "Fecha de pago", auto_now_add=True, blank=False, null=False)
    usuarios = models.OneToOneField(to=User, on_delete=models.CASCADE)


class Facturacion_mensual(models.Model):
    id_usuario = models.IntegerField("Id usuario", blank=False, null=False)
    tipo_usuario = models.CharField(
        "Tipo Usuario", max_length=1, blank=False, null=False)
    id_pedido = models.IntegerField("Id pedido", blank=False, null=False)
    fecha_transaccion = models.DateField(
        "Fecha transaccion", auto_now_add=True, blank=False, null=False)
    monto_facturado = models.IntegerField(
        "Monto Facturado",  blank=False, null=False)
