# Generated by Django 4.2.2 on 2023-08-07 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('creation_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
