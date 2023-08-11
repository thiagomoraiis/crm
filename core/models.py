from django.db import models # noqa
from custom_user.models import CustomUser


class Invoicing(models.Model):
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
        max_digits=22, decimal_places=2
    )
    client = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL,
        null=True, blank=True, default=''
    )

    def __str__(self) -> str:
        return f'{self.title} - {self.value} - {self.client.username}'
