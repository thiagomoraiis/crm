# Generated by Django 4.2.2 on 2023-08-10 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_revenue_invoicing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoicing',
            name='client',
        ),
    ]
