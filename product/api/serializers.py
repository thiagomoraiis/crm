from rest_framework import serializers
from ..models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id', 'name', 'slug', 'price',
            'description', 'category',
            'creation_date', 'posted_by',
            # 'tags', 'discount_price'
        )
