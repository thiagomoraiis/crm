from django.shortcuts import render, get_object_or_404 # noqa
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.db.models import Sum # noqa
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import DeleteView, UpdateView, CreateView, ListView
from core.models import Transactions, Inventory
from product.models import Product
from cart.models import Cart, CartItem
from datetime import datetime


class DashboardListView(UserPassesTestMixin, ListView):
    """
    A class-based view that displays a dashboard template
        with transaction data.

    This view requires the user to be a staff member to access.
    It retrieves transaction data for the current month and
    calculates the total sum of values.
    """
    template_name = 'core/pages/dashboard.html'
    context_object_name = 'total'

    def get_queryset(self):
        """
        Retrieves a queryset of transactions for the current month
        and calculates the total value of those transactions.

        Returns:
        float: The total value of transactions for the current month,
        rounded to two decimal places.
            Returns 0.0 if there are no transactions for the current month.
        """
        current_month = datetime.today().month
        qs = Transactions.objects.filter(date__month=current_month)

        if qs:
            total_value = qs.aggregate(sum_value=Sum('value'))['sum_value']
            total_value = round(total_value, 2)

        return total_value

    def test_func(self):
        """
        Check if the user is a staff member.

        Returns:
            bool: True if the user is a staff member, False otherwise.
        """
        return self.request.user.is_staff


class IndexListView(ListView):
    """
    A class-based view that renders the index page and displays
    a list of products.

    Attributes:
    template_name (str): The path to the HTML template for rendering the view.
    context_object_name (str): The name to be used for the products list in
        the template context.
    queryset (QuerySet): The queryset containing the list of products
        to be displayed.
    paginate_by (int): The number of products to display per page.
    """
    template_name = 'core/pages/index.html'
    context_object_name = 'products'
    queryset = Product.objects.all()
    paginate_by = 12

    def get_context_data(self, **kwargs):
        """
        Augments the context with additional data related to the
        user's cart and cart items.

        Args:
        **kwargs: Additional keyword arguments to be passed to the
        parent's `get_context_data` method.

        Returns:
        dict: The augmented context data.
        """
        context = super().get_context_data(**kwargs)
        self.add_cart_to_context(context)

        return context

    def add_cart_to_context(self, context):
        """
        Adds cart-related information to the context if the user
        is authenticated.

        Args:
        context (dict): The context dictionary to be augmented.
        """
        if self.request.user.is_authenticated:
            cart, cart_items = self.get_cart_info()

            if cart:
                total_product_in_cart = cart_items.aggregate(
                    quantity_sum=Sum('quantity'))['quantity_sum']
                context['total_product_in_cart'] = total_product_in_cart
                context['cart_items'] = cart_items.count()

    def get_cart_info(self):
        """
        Retrieves the user's cart and cart items.

        Returns:
        tuple: A tuple containing the user's cart and a queryset of cart items.
               If the user's cart or cart items are not found, returns
               (None, None).
        """
        try:
            cart = Cart.objects.get(cart_owner=self.request.user)
            cart_items = CartItem.objects.filter(cart=cart)
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
    """
    A class-based view that allows the creation of inventory records
    by authorized superusers.

    Attributes:
    template_name (str): The path to the HTML template for rendering
    the view.
    fields (list): The fields of the inventory model that will be
    displayed in the form.
    model (Model): The Django model associated with the view for which
    records are being created.
    success_url (str): The URL to redirect to after a successful
    form submission.
    """
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
    """
    A class-based view that allows deletion of inventory records by
    authorized staff users.

    Attributes:
    model (Model): The Django model associated with the view for which
    records are being deleted.
    template_name (str): The path to the HTML template for rendering
    the delete confirmation view.
    success_url (str): The URL to redirect to after a successful record
    deletion.
    context_object_name (str): The name to be used for the inventory record
    in the template context.
    pk_url_kwarg (str): The URL keyword argument name for the primary key
    of the inventory record to be deleted.
    """
    model = Inventory
    template_name = 'core/pages/inventory_delete_confirmation.html'
    success_url = reverse_lazy('core:inventory-list')
    context_object_name = 'inventory'
    pk_url_kwarg = 'id'

    def test_func(self):
        return self.request.user.is_staff


class InventoryListView(ListView):
    """
    A class-based view that displays a list of inventory records
    with associated products.

    Attributes:
    template_name (str): The path to the HTML template for
    rendering the view.
    context_object_name (str): The name to be used for the
    inventory records list in the template context.
    model (Model): The Django model associated with the view
    for which records are being listed.
    queryset (QuerySet): The queryset containing the list
    of inventory records to be displayed.
    paginate_by (int): The number of inventory records to
    display per page.
    """
    template_name = 'core/pages/inventory_list.html'
    context_object_name = 'inventory'
    model = Inventory
    queryset = Inventory.objects.all()
    paginate_by = 15

    def get_queryset(self):
        """
        Retrieves the queryset of inventory records and performs a
        select_related operation to fetch associated products efficiently.

        Returns:
        QuerySet: The queryset of inventory records with associated products.
        """
        qs = super().get_queryset()
        qs = qs.select_related('product')
        return qs
