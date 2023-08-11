# flake8: noqa
from django.contrib import admin
from .models import Invoicing


@admin.register(Invoicing)
class InvoicingAdmin(admin.ModelAdmin):
    list_display = ('title', 'type_revenue', 'value')