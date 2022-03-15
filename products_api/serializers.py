from rest_framework import serializers
from .models import Product, SoftFurniture, Armchair


class SoftFurnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftFurniture
        fields = ('id', 'slug', 'type', 'title', 'image', 'height', 'width', 'depth', 'seat_depth', 'container',
                  'headrest', 'arm', 'sleep_func', 'sleep_dim')


class ArmchairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Armchair
        fields = ('id', 'slug', 'type', 'title', 'image', 'height', 'width', 'depth', 'seat_depth', 'container',
                  'headrest', 'trim')



class ProductSerializer(serializers.ModelSerializer):
    sofas = SoftFurnsSerializer()
    armchairs = ArmchairSerializer()

    class Meta:
        model = Product
        fields = '__all__'
