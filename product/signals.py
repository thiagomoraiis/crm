from django.template.defaultfilters import slugify # noqa
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Product, Discounts
#
#
# @receiver(post_save, sender=Discounts)
# def discount_to_products(sender, instance, **kwargs):
#     if instance.value is not None:
#         discount = instance.value
#
#         for product in Product.objects.all():
#             product.discount_price = discount
#             product.save()
