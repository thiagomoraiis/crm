from django.db import models
from django.contrib.auth.models import User
from product.models import Product


class Transactions(models.Model):
    CHOICES_TYPE_REVENUE = (
        ('revenue', 'Revenue'),
        ('expense', 'Expense')
    )

    title = models.CharField(
        max_length=150, blank=True,
        default=''
    )
    type_revenue = models.CharField(
        max_length=10, choices=CHOICES_TYPE_REVENUE,
        default='revenue'
    )
    date = models.DateTimeField(
        auto_now_add=True
    )
    value = models.DecimalField(
        max_digits=8, decimal_places=2
    )
    client = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, blank=True
    )

    def __str__(self) -> str:
        return f'{self.title} - {self.value} - {self.client}'


class Inventory(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(
        blank=True, default=0
    )

    def __str__(self) -> str:
        return f'{self.product.name} - {self.quantity}'


class Company(models.Model):
    owner = models.OneToOneField(
        User, on_delete=models.SET_NULL,
        null=True, blank=False
    )
    name = models.CharField(max_length=150)
    email = models.EmailField()
    total_value = models.DecimalField(
        max_digits=22, decimal_places=2,
        default=0.00
    )

    def __str__(self) -> str:
        return f'{self.name} {self.owner}'

    def save(self, *args, **kwargs):
        if not self.id and Company.objects.exists():
            return

        return super().save(*args, **kwargs)
