# from django.shortcuts import render
from product.models import Product
# from .forms import ProductModelForm
from django.urls import reverse_lazy
from django.views.generic import (
                DeleteView, DetailView,
                CreateView, UpdateView)


class ProductDetailView(DetailView):
    template_name = 'core/pages/product.html'
    model = Product
    context_object_name = 'product'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class ProductCreateView(CreateView):
    template_name = 'core/pages/product_form.html'
    fields = [
        'name', 'price', 'description',
        'stock', 'image', 'category',
        'posted_by', 'tags'
    ]
    model = Product
    success_url = reverse_lazy('core:product-list')


class ProductUpdateView(UpdateView):
    template_name = 'core/pages/product_form.html'
    fields = [
        'name', 'price', 'description',
        'stock', 'image', 'category',
        'posted_by', 'tags'
    ]
    model = Product
    context_object_name = 'product'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('core:product-list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'core/pages/product_delete.html'
    success_url = reverse_lazy('core:product-list')
    context_object_name = 'product'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
