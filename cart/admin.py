from django.contrib import admin
from .models import Cart, CartItem
from customer.models import HistoricItem, PurchaseHistoric


class HistoricItemInline(admin.TabularInline):
    model = HistoricItem


@admin.register(PurchaseHistoric)
class PurchaseHistoricAdmin(admin.ModelAdmin):
    inlines = [HistoricItemInline]


@admin.register(HistoricItem)
class HistoricItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'date')


class CartItemInline(admin.TabularInline):
    model = CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product_item', 'cart', 'quantity', 'total_price_item')
