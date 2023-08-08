from django.shortcuts import render, get_object_or_404 # noqa
from django.views.generic import (TemplateView, ListView)
from django.contrib.auth.mixins import UserPassesTestMixin
from product.models import Product
from cart.models import Cart, CartItem
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.core.exceptions import ObjectDoesNotExist


class DashboardTemplateView(UserPassesTestMixin, TemplateView):
    template_name = 'core/pages/dashboard.html'

    def test_func(self):
        return self.request.user.is_staff


class IndexListView(ListView):
    template_name = 'core/pages/index.html'
    context_object_name = 'products'
    model = Product
    queryset = Product.objects.all()

    # @method_decorator(login_required, name='post')
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            try:
                cart = Cart.objects.get(cart_owner=self.request.user)
                total_product_in_cart = CartItem.objects.filter(
                    cart=cart).aggregate(Sum('quantity'))['quantity__sum']
                context['total_product_in_cart'] = total_product_in_cart
                print(self.request.user)
                return context
            except ObjectDoesNotExist:
                return context
        else:
            return context


class RegisterTemplateView(TemplateView):
    template_name = 'core/pages/register.html'


class ProductListView(UserPassesTestMixin, ListView):
    template_name = 'core/pages/list_products.html'
    context_object_name = 'products'
    queryset = Product.objects.all()

    def test_func(self):
        return self.request.user.is_staff
