from django.shortcuts import render, get_object_or_404 # noqa
from django.views.generic import (TemplateView, ListView)
from product.models import Product


class DashboardTemplateView(TemplateView):
    template_name = 'core/pages/dashboard.html'


class IndexListView(ListView):
    template_name = 'core/pages/index.html'
    context_object_name = 'products'
    model = Product
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class RegisterTemplateView(TemplateView):
    template_name = 'core/pages/register.html'


class ProductListView(ListView):
    template_name = 'core/pages/list_products.html'
    context_object_name = 'products'
    queryset = Product.objects.all()
