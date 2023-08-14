from django.contrib import admin
from .models import Product, Tag, Inventory


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'product')
