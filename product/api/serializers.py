from rest_framework import serializers
from ..models import Product


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id', 'name', 'slug', 'price',
            'discount_price', 'description',
            'category', 'creation_date',
            'posted_by', 'tags', 'discount_price'
        )
