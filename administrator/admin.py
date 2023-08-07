from django.contrib import admin
from .models import Office

# @admin.register(AdministratorUser)
# class AdministratorUserAdmin(admin.ModelAdmin):
#     list_display = ('office', )


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('name', )
