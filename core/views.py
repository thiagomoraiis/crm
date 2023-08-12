from django.shortcuts import render, get_object_or_404 # noqa
from django.views.generic import (TemplateView, ListView)
from django.contrib.auth.mixins import UserPassesTestMixin
from core.models import Transactions, Invoicing
from product.models import Product
from cart.models import Cart, CartItem
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.core.exceptions import ObjectDoesNotExist


class DashboardTemplateView(UserPassesTestMixin, ListView):
    template_name = 'core/pages/dashboard.html'
    queryset = Invoicing.objects.values('total_value')
    context_object_name = 'total'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.first()['total_value']

    def test_func(self):
        return self.request.user.is_staff


class IndexListView(ListView):
    template_name = 'core/pages/index.html'
    context_object_name = 'products'
    model = Product
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            try:
                cart = Cart.objects.get(
                    cart_owner=self.request.user
                )
                cart_items = CartItem.objects.filter(
                    cart=cart
                )
                total_product_in_cart = cart_items.aggregate(
                    Sum('quantity'))['quantity__sum']

                context['total_product_in_cart'] = total_product_in_cart
                context['cart_items'] = cart_items.count()
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


class TransactionsListView(ListView):
    template_name = 'core/pages/invoicing_list.html'
    model = Transactions
    queryset = Transactions.objects.all()
    context_object_name = 'transactions'
