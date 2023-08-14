from django.shortcuts import render, get_object_or_404 # noqa
from django.views.generic import (TemplateView, ListView)
from django.contrib.auth.mixins import UserPassesTestMixin
from core.models import Transactions
from product.models import Product
from cart.models import Cart, CartItem
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
from django.db.models import Sum # noqa
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime


class DashboardTemplateView(UserPassesTestMixin, ListView):
    template_name = 'core/pages/dashboard.html'
    queryset = Transactions.objects.values('value', 'date')
    context_object_name = 'total'

    def get_queryset(self):
        qs = super().get_queryset()
        current_month = datetime.today().month
        qs.values('value', 'date').filter(date__month=current_month)

        qs = round(qs.values('value').aggregate(
            sum_value=Sum('value')
        )['sum_value'], 2)

        return qs

    def test_func(self):
        return self.request.user.is_staff


class IndexListView(ListView):
    template_name = 'core/pages/index.html'
    context_object_name = 'products'
    model = Product
    queryset = Product.objects.all()
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.add_cart_to_context(context)

        return context

    def add_cart_to_context(self, context):
        if self.request.user.is_authenticated:
            cart, cart_items = self.get_cart_info()

            if cart:
                total_product_in_cart = cart_items.aggregate(
                    Sum('quantity'))['quantity__sum']
                context['total_product_in_cart'] = total_product_in_cart
                context['cart_items'] = cart_items.count()

    def get_cart_info(self):
        try:
            cart = Cart.objects.get(
                cart_owner=self.request.user
            )
            cart_items = CartItem.objects.filter(
                cart=cart
            )
            return cart, cart_items
        except ObjectDoesNotExist:
            return None, None


class RegisterTemplateView(TemplateView):
    template_name = 'core/pages/register.html'


class ProductListView(UserPassesTestMixin, ListView):
    template_name = 'core/pages/list_products.html'
    context_object_name = 'products'
    queryset = Product.objects.all()
    paginate_by = 10

    def test_func(self):
        return self.request.user.is_staff


class TransactionsListView(ListView):
    template_name = 'core/pages/transactions_list.html'
    model = Transactions
    queryset = Transactions.objects.all()
    context_object_name = 'transactions'
    paginate_by = 9
