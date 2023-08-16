from django.shortcuts import render, get_object_or_404 # noqa
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from core.models import Transactions, Inventory
from product.models import Product
from cart.models import Cart, CartItem
from django.db.models import Sum # noqa
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from django.views.generic import DeleteView, UpdateView, CreateView, ListView
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required


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


class TransactionsListView(ListView):
    template_name = 'core/pages/transactions_list.html'
    model = Transactions
    queryset = Transactions.objects.all()
    context_object_name = 'transactions'
    paginate_by = 9


class InventoryCreateView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    template_name = 'core/pages/inventory_form.html'
    fields = [
        'product', 'quantity'
    ]
    model = Inventory
    success_url = reverse_lazy('core:inventory-list')

    def test_func(self):
        return self.request.user.is_superuser


class InventoryUpdateView(UserPassesTestMixin, UpdateView):
    template_name = 'core/pages/inventory_form.html'
    fields = [
        'product', 'quantity'
    ]
    model = Inventory
    context_object_name = 'inventory'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('core:inventory-list')

    def test_func(self):
        return self.request.user.is_staff


class InventoryDeleteView(UserPassesTestMixin, DeleteView):
    model = Inventory
    template_name = 'core/pages/inventory_delete_confirmation.html'
    success_url = reverse_lazy('core:inventory-list')
    context_object_name = 'inventory'
    pk_url_kwarg = 'id'

    def test_func(self):
        return self.request.user.is_staff


class InventoryListView(ListView):
    template_name = 'core/pages/inventory_list.html'
    context_object_name = 'inventory'
    model = Inventory
    queryset = Inventory.objects.all()
    paginate_by = 15
