from rest_framework import serializers
from .models import Region, Comuna, User, Delivery, Cliente, Restaurante, Direcciones, Producto, Medio_Pago, Pedido, Detalle_Pago, Detalle_Pedido, Facturado, Facturacion_mensual


# serializars from models import from api rappidos


class Region_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

        # overwrite method view endpoints

        # def to_representation(self,instance):
        #     return {

        #     }


class Comuna_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = '__all__'

        # overwrite method view endpoints

        # def to_representation(self,instance):
        #     return {

        #     }


class User_Serializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'tipo', 'is_active')

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            password=validated_data['password'],
            tipo=validated_data['tipo'],
            is_active=validated_data['is_active']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        update_user = super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user

        # overwrite method view endpoints

        # def to_representation(self,instance):
        #     return {

        #     }


class Delivery_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'

        # overwrite method view endpoints

        # def to_representation(self,instance):
        #     return {

        #     }


class Cliente_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

        # overwrite method view endpoints

        # def to_representation(self,instance):
        #     return {

        #     }


class Restaurante_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = '__all__'

        # overwrite method view endpoints

        # def to_representation(self,instance):
        #     return {

        #     }


class Direcciones_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Direcciones
        fields = '__all__'

        # overwrite method view endpoints

        # def to_representation(self,instance):
        #     return {

        #     }


class Producto_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

        # overwrite method view endpoints

        # def to_representation(self,instance):
        #     return {

        #     }


class Medio_Pago_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Medio_Pago
        fields = '__all__'

        # overwrite method view endpoints

        # def to_representation(self,instance):
        #     return {

        #     }


class Pedido_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

        # overwrite method view endpoints

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "estado": instance.estado,
            "direccion_restaurante": instance.restaurante.direccion_restaurante,
            "id_restaurante": instance.restaurante.id,
            "id_cliente": instance.cliente.id,
            "nombre_cliente": f'{instance.cliente.nombre_cliente} {instance.cliente.apellidos_cliente}',
            "delivery": instance.delivery.id,
            "monto_envio": instance.monto_envio,
            "monto_total_pedido": instance.monto_total_pedido,
        }


class Detalle_Pago_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Detalle_Pago
        fields = '__all__'

        # overwrite method view endpoints

        # def to_representation(self,instance):
        #     return {

        #     }


class Detalle_Pedido_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Detalle_Pedido
        fields = '__all__'

        # overwrite method view endpoints

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'id_pedido': instance.pedido.id,
            'id_producto': instance.producto.id,
            'nombre_producto': instance.producto.nombre_producto,
            'precio_venta': instance.producto.precio_venta_producto,
            'descripcion_producto': instance.producto.descripcion_producto,
            'imagen_producto': instance.producto.imagen_producto
        }


class Facturado_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Facturado
        fields = '__all__'

        # overwrite method view endpoints

        # def to_representation(self,instance):
        #     return {

        #     }


class Facturacion_mensual_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Facturacion_mensual
        fields = '__all__'

        # overwrite method view endpoints

        # def to_representation(self,instance):
        #     return {

        #     }
