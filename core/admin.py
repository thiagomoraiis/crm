# flake8: noqa
from django.contrib import admin
from .models import Inventory, Transactions, Billing, Company


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'type_revenue', 'value', 'client')

    def client(self, obj):
        return obj.client.username


@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = ('total_value',)


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'product')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'owner')