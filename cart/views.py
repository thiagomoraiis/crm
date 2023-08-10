from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, View
from cart.models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Sum


class CartView(View):
    def get_products(self, request):
        if self.request.user.is_authenticated:
            try:
                cart = Cart.objects.filter(
                    cart_owner=self.request.user
                ).first()
                products = CartItem.objects.filter(
                    cart=cart
                )
                return products

            except ObjectDoesNotExist:
                pass

    def get(self, request):
        product_cart = self.get_products(request)
        products_total_cart = product_cart.aggregate(
            total_price_sum=Sum('total_price_item')
        )['total_price_sum']

        return render(
            request, 'cart/pages/cart.html',
            {'products': product_cart,
             'quantity': product_cart.count(),
             'products_total_cart': round(products_total_cart, 2),
             }
        )

    def post(self, request):
        product_cart = self.get_products(request)

        return render(
            request, 'cart/pages/cart.html',
            {'products': product_cart}
        )


def remove_item(request, id):
    product = get_object_or_404(CartItem, id=id)
    product.delete
    return redirect('core:index')

# class CartListView(ListView):
#     template_name = 'cart/pages/cart.html'
#     context_object_name = 'products'
#     model = CartItem
#
#     def get_queryset(self):
#         if self.request.user.is_authenticated:
#             try:
#                 cart = Cart.objects.get(
#                     cart_owner=self.request.user
#                 )
#                 cart_items = CartItem.objects.filter(
#                     cart=cart
#                 )
#                 return cart_items
#             except ObjectDoesNotExist:
#                 return super().self.get_queryset()
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['quantity'] = self.get_queryset().count()
#         return context
