from rest_framework import serializers
from .models import Product, SoftFurniture, Armchair


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')
        extra_fields = ['slug']

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(ProductSerializer, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields

# 'id', 'title', 'image', 'height', 'width', 'depth', 'seat_depth', 'container', 'headrest', 'type',
#                   'arm', 'sleep_func', 'sleep_dim', 'trim'
