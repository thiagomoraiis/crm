from django.db import models
from django.contrib.auth.models import User
from product.models import Product


class Cart(models.Model):
    cart_owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    cart_product = models.ManyToManyField(
        Product, through='CartItem'
    )

    def __str__(self):
        return f'{self.cart_product.name}'


class CartItem(models.Model):
    product_item = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(
        'Cart Quantity'
    )
    total_price_item = models.DecimalField(
        'Total Item Price', max_digits=10, decimal_places=2,
        default=0.00
    )

    def __str__(self):
        return f'{self.product_item.name}'

    def save(self, *args, **kwargs):
        if not self.total_price_item:
            self.total_price_item = self.quantity * self.product_item.price
        return super().save(*args, **kwargs)
