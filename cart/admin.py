from django.contrib import admin
from .models import Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product_item', 'cart', 'quantity', 'total_price_item')
