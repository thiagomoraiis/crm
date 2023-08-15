from django.db import models
from custom_user.models import CustomUser
from django.template.defaultfilters import slugify
from decimal import Decimal
from uuid import uuid1


DISCOUNT_PERCENTAGE = 10


class Tag(models.Model):
    name = models.CharField(
        max_length=50
    )

    def __str__(self) -> str:
        return self.name


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
    discount_price = models.DecimalField(
        'Discount Price', max_digits=7,
        decimal_places=2, blank=True, default=0.00
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
        CustomUser, on_delete=models.CASCADE
    )
    creation_date = models.DateField(
        'Date of Insert',
        auto_now_add=True
    )
    tags = models.ManyToManyField(
        Tag, blank=True
    )

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            unique_uuid = uuid1()
            self.slug = f'{slugify(self.name)}-{unique_uuid}'

        if not self.discount_price:
            discount_price = self.discount_price
            discount_price = (Decimal(str(
                round(DISCOUNT_PERCENTAGE / 100, 2)
            ))) * self.price
            self.discount_price = discount_price
            print(self.discount_price)

        return super().save(*args, **kwargs)
