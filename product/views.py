from django.shortcuts import render, get_object_or_404
from product.models import Product
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (DeleteView, View,
                                  CreateView, UpdateView, ListView)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from cart.models import Cart, CartItem


class ProductDetailView(View):
    def get_product(self, request, slug):
        product = get_object_or_404(
            Product, slug=slug
        )
        return product

    @method_decorator(login_required, name='post')
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, slug):
        product = self.get_product(request, slug)
        context = {'product': product}
        return render(request, 'product/pages/product.html', context)

    def post(self, request, slug):
        product = self.get_product(request, slug)
        quantity = int(self.request.POST.get('quantity', ''))
        cart, created = Cart.objects.get_or_create(
            cart_owner=self.request.user
        )

        self.update_or_create_item_product(cart, product, quantity)

        return render(
            request, 'product/pages/product.html',
            {'product': product}
        )

    def update_or_create_item_product(self, cart, product, quantity):
        item_cart = CartItem.objects.filter(
            product_item=product, cart=cart
        ).first()

        if item_cart:
            item_cart.quantity += quantity
            item_cart.total_price_item = \
                item_cart.quantity * item_cart.product_item.price
            item_cart.save()
        else:
            item_cart = CartItem.objects.create(
                product_item=product, cart=cart,
                quantity=quantity
            )


class ProductCreateView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    template_name = 'product/pages/product_form.html'
    fields = [
        'name', 'price', 'description',
        'image', 'category',
    ]
    model = Product
    success_url = reverse_lazy('core:inventory-list')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser


class ProductUpdateView(UserPassesTestMixin, UpdateView):
    template_name = 'product/pages/product_form.html'
    fields = [
        'name', 'price', 'description',
        'image', 'category',
    ]
    model = Product
    context_object_name = 'product'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('product:product-list')

    def test_func(self):
        return self.request.user.is_superuser


class ProductDeleteView(UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'product/pages/product_delete.html'
    success_url = reverse_lazy('product:product-list')
    context_object_name = 'product'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def test_func(self):
        return self.request.user.is_superuser


class ProductListView(UserPassesTestMixin, ListView):
    template_name = 'product/pages/list_products.html'
    context_object_name = 'products'
    queryset = Product.objects.all()
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('posted_by')
        return qs

    def test_func(self):
        return self.request.user.is_superuser
