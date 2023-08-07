from django.db import models
# from django.contrib.auth.models import User
from custom_user.models import CustomUser
from product.models import Product


class Cart(models.Model):
    cart_owner = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE
    )
    cart_product = models.ManyToManyField(
        Product, through='CartItem'
    )
    status = models.CharField(
        max_length=20,
        choices=(('open', 'Open'), ('close', 'Close'))
    )

    def __str__(self):
        return f'{self.cart_product}'


class CartItem(models.Model):
    product_item = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField('Cart Quantity')
    total_cart_item = models.PositiveIntegerField('Total Item Price')

    def __str__(self):
        return f'{self.product_item}'
