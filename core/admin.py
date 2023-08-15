# flake8: noqa
from django.contrib import admin
from .models import Inventory, Transactions, Invoicing


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'type_revenue', 'value', 'client')

    def client(self, obj):
        return obj.client.username


@admin.register(Invoicing)
class InvoicingAdmin(admin.ModelAdmin):
    list_display = ('total_value',)


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'product')
