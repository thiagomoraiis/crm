from rest_framework import serializers
from ..models import Product
from core.models import Inventory


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['quantity', ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id', 'name', 'slug', 'price',
            'description', 'category',
            'creation_date', 'posted_by',
            'image',
        )
        read_only_fields = ('slug', 'posted_by')
