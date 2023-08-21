from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=150, unique=True
    )
    first_name = models.CharField(
        max_length=150, blank=True
    )
    last_name = models.CharField(
        max_length=150, blank=True
    )
    telephone = models.CharField(
        max_length=16, blank=True
    )
    email = models.EmailField(
        blank=True, unique=True
    )
    city = models.CharField(
        max_length=150
    )
    address = models.CharField(
        max_length=150
    )
    creation_date = models.DateField(
        auto_created=True,
        blank=True, null=True
    )
    password = models.CharField(
        max_length=128
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        if self.password:
            self.password = self.set_password(self.password)
        return super().save(*args, **kwargs)
