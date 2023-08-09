from django.db import models
from custom_user.models import CustomUser


class Tasks(models.Model):
    PRIORITY_CHOICES = (
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low')
    )

    task_name = models.CharField(
        'Task:', max_length=100
    )
    description = models.TextField(
        'Description: '
    )
    priority_level = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES
    )
    creation_date = models.DateField(
        auto_now_add=True
    )
    completion_date = models.DateField(
        auto_now=True
    )
    is_finish = models.BooleanField(
        default=False
    )
    responsible = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self) -> str:
        return self.task_name
