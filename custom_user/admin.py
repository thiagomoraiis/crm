# flake8: noqa
from django.contrib import admin 
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'creation_date', 'telephone')

