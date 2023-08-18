from rest_framework import serializers
from ..models import Inventory, Invoicing


class InventoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = [
            'product', 'quantity'
        ]


class InvoicingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoicing
        fields = [
            'total_value'
        ]
