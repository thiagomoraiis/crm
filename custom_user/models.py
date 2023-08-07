from django.db import models
from django.contrib.auth.models import AbstractUser
from administrator.models import Office


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=150, unique=True
    )
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    telephone = models.CharField(max_length=16, blank=True)
    email = models.EmailField(blank=True, unique=True)
    city = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    office = models.ForeignKey(
        Office, on_delete=models.SET_NULL,
        null=True, blank=True
    )
    creation_date = models.DateField(
        auto_created=True, blank=True, null=True
    )
    password = models.CharField("password", max_length=128)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
