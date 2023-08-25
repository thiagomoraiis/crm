from rest_framework import serializers
from ..models import Inventory, Company
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name',
            'username', 'email', 'password'
        ]


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = [
            'id', 'product', 'name', 'quantity'
        ]
    name = serializers.StringRelatedField()


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'id', 'owner', 'name', 'total_value'
        ]
