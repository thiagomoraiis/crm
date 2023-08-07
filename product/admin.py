from django.contrib import admin
from .models import Product, ProductCategory, Tag


# @admin.register(Discounts)
# class DiscountsAdmin(admin.ModelAdmin):
#     list_display = ('name', 'value')


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
