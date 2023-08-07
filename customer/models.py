from django.db import models # noqa

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
