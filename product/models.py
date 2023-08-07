from django.db import models
from custom_user.models import CustomUser
from django.template.defaultfilters import slugify
# from django.contrib.auth.models import User


class ProductCategory(models.Model):
    category_name = models.CharField('Product Category', max_length=50)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    name = models.CharField('Name of Product', max_length=150)
    price = models.DecimalField('Price', max_digits=7, decimal_places=2)
    description = models.TextField('Description of roduct')
    stock = models.PositiveIntegerField('Product Stock')
    image = models.ImageField(upload_to='product')
    slug = models.SlugField('Slug', editable=False, unique=True, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

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

        return super().save(*args, **kwargs)
