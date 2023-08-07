from django.db import models


class ContactCustomer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    city = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
