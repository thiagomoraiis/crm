# flake8: noqa
from django.contrib import admin
from .models import Inventory, Transactions, Company


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'type_revenue', 'value', 'client')

    def client(self, obj):
        return obj.client.username


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'total_value',)

    def name(self, obj):
        return obj.owner.username


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'product')


# @admin.register(Company)
# class CompanyAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'owner')