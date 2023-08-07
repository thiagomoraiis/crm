from django.db import models
# from core.models import CustomUser


class Office(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name


# class AdministratorUser(CustomUser):
#     office = models.ForeignKey(
#         Office, on_delete=models.SET_NULL,
#         null=True, blank=True
#     )

#     def __str__(self) -> str:
#         return f'{self.first_name.capitalize()}
#           {self.last_name.capitalize()}'
