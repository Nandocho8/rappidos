from rest_framework import serializers
from .models import Region,Comuna,User,Delivery,Cliente,Restaurante,Direcciones,Producto,Medio_Pago,Pedido,Detalle_Pago,Detalle_Pedido,Facturado,Facturacion_mensual


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
        fields = '__all__'

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

        # def to_representation(self,instance):
        #     return {

        #     }


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

        # def to_representation(self,instance):
        #     return {

        #     }


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

