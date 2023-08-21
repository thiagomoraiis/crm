from rest_framework import serializers
from ..models import Inventory, Invoicing
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name',
            'username', 'email', 'password'
        ]


class InventoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = [
            'id', 'product', 'quantity'
        ]


class InvoicingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoicing
        fields = [
            'id', 'total_value'
        ]
