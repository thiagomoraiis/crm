from django.db import models
from custom_user.models import CustomUser
from django.template.defaultfilters import slugify
from decimal import Decimal


DISCOUNT_PERCENTAGE = 10


# class Discounts(models.Model):
#     name = models.CharField(max_length=100)
#     value = models.DecimalField(max_digits=5, decimal_places=2)
#
#     def __str__(self):
#         return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class ProductCategory(models.Model):
    category_name = models.CharField('Product Category', max_length=50)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    name = models.CharField('Name of Product', max_length=150)
    price = models.DecimalField(
        'Price', max_digits=7,
        decimal_places=2
    )
    discount_price = models.DecimalField(
        'Discount Price', max_digits=7,
        decimal_places=2, blank=True, default=0.00
    )
    description = models.TextField('Description of roduct')
    stock = models.PositiveIntegerField('Product Stock')
    image = models.ImageField(upload_to='product')
    slug = models.SlugField(
        'Slug', editable=False,
        unique=True, blank=True
    )
    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE
    )
    posted_by = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE
    )
    creation_date = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f'{slugify(self.name)}'
        slug = self.slug
        counter = 1
        while self.__class__.objects.filter(slug=self.slug).exists():
            self.slug = f'{slug}-{counter}'
            counter += 1

        if not self.discount_price:
            discount_price = self.discount_price
            discount_price = (Decimal(str(round(DISCOUNT_PERCENTAGE / 100, 2)))) * self.price # noqa
            self.discount_price = discount_price
            print(self.discount_price)
        return super().save(*args, **kwargs)

    # def get_discount_price(self):
    #     discount_price = Discounts.objects.first()
    #     if discount_price:
    #         discount_value = discount_price.value
    #         self.discount_price = self.price * (discount_value / 100)
    #         return self.discount_price
#
    #     return self.discount_price
