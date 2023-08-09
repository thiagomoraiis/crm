from django.db import models # noqa
from custom_user.models import CustomUser
from product.models import Product


class PurchaseHistoric(models.Model):
    owner = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE
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
    historic = models.ForeignKey(PurchaseHistoric, on_delete=models.CASCADE)
    date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self) -> str:
        return self.product.name

#
# class Customer(models.Model):
#     GENDER_CHOICES = (
#         ('masculine', 'Masculine'),
#         ('feminine', 'Feminine'),
#     )
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     gender = models.CharField(
#         max_length=10, choices=GENDER_CHOICES,
#         null=True, blank=True
#     )
#     creation_date = models.DateField(
#           auto_now_add=True, null=True, blank=True)
#     telephone = models.CharField(max_length=16)
#
#     def __str__(self) -> str:
#         return f'{self.first_name} {self.last_name}'
