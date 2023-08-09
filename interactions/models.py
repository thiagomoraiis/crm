from django.db import models
from custom_user.models import CustomUser


class Interaction(models.Model):
    customer = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE
    )
    interaction_type = models.CharField(
        max_length=50
    )
    notes = models.TextField()
    date_created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.interaction_type} - {self.customer}"
