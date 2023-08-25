from django.db import models
from django.contrib.auth.models import User
from product.models import Product


class Cart(models.Model):
    """
    A model representing a user's shopping cart.

    Attributes:
    cart_owner (User): The user who owns the shopping cart.
    cart_product (ManyToManyField): The products in the shopping cart.
    """
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
    """
    A model representing an item in a user's shopping cart.

    Attributes:
    product_item (Product): The product associated with the cart item.
    cart (Cart): The shopping cart to which the cart item belongs.
    quantity (PositiveIntegerField): The quantity of the product in
    the cart item.
    total_price_item (DecimalField): The total price of the cart item.
    """
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
        """
        Custom save method for the CartItem model.

        This method calculates and sets the total price of the cart item
        if it is not already set.

        Args:
        *args: Additional positional arguments that might be passed to
        the parent's `save` method.
        **kwargs: Additional keyword arguments that might be passed to
        the parent's `save` method.

        Returns:
        Model: The saved CartItem instance, returned by calling the
        parent's `save` method.
        """
        if not self.total_price_item:
            self.total_price_item = self.quantity * self.product_item.price
        return super().save(*args, **kwargs)
