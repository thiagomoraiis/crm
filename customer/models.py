from django.db import models # noqa
from django.contrib.auth.models import User
from product.models import Product


class PurchaseHistoric(models.Model):
    owner = models.OneToOneField(
        User, on_delete=models.CASCADE
    )
    product_list = models.ManyToManyField(
        Product, through='HistoricItem'
    )

    def __str__(self) -> str:
        return self.owner.username


class HistoricItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
    )
    historic = models.ForeignKey(
        PurchaseHistoric, on_delete=models.CASCADE
    )
    date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self) -> str:
        return self.product.name


class ContactCustomer(models.Model):
    first_name = models.CharField(
        max_length=100
    )
    last_name = models.CharField(
        max_length=150
    )
    email = models.EmailField()
    telephone = models.CharField(
        max_length=20
    )
    city = models.CharField(
        max_length=150
    )
    address = models.CharField(
        max_length=150
    )
    creation_date = models.DateField(
        auto_now_add=True
    )

    def __str__(self) -> str:
        return self.name
