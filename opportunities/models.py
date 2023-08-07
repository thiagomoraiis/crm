from django.db import models
# from django.contrib.auth.models import User
from custom_user.models import CustomUser


class Opportunity(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    closing_date = models.DateField()

    def __str__(self):
        return self.name
