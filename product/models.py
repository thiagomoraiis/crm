from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from uuid import uuid1


class Product(models.Model):
    CHOICES_PRODUCT_CATEGORY = (
        ('smartphone', 'Smartphone'),
        ('notebook', 'Notebook'),
        ('refrigerator', 'Refrigerator'),
        ('stove', 'Stove')
    )
    name = models.CharField(
        'Name of Product', max_length=150
    )
    price = models.DecimalField(
        'Price', max_digits=7,
        decimal_places=2
    )
    description = models.TextField(
        'Description'
    )
    image = models.ImageField(
        'Image',
        upload_to='product/%y/%m/%d'
    )
    slug = models.SlugField(
        'Slug', editable=False,
        unique=True, blank=True
    )
    category = models.CharField(
        'Category', max_length=20,
        choices=CHOICES_PRODUCT_CATEGORY,
    )
    posted_by = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    creation_date = models.DateField(
        'Date of Insert', auto_now_add=True
    )

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            unique_uuid = uuid1()
            self.slug = f'{slugify(self.name)}-{unique_uuid}'

        return super().save(*args, **kwargs)
