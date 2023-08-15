from django.urls import path # noqa
from .views import (ProductCreateView, ProductDetailView, ProductUpdateView,
                    ProductListView, ProductDeleteView)

app_name = 'product'

urlpatterns = [
    path(
        'create/',
        ProductCreateView.as_view(),
        name='product-create'),
    path(
        'update/<slug:slug>/',
        ProductUpdateView.as_view(),
        name='product-update'
    ),
    path(
        'delete/<slug:slug>/',
        ProductDeleteView.as_view(),
        name='product-delete'
    ),
    path(
        'list/',
        ProductListView.as_view(),
        name='product-list'
    ),
    path(
        '<slug:slug>/',
        ProductDetailView.as_view(),
        name='product-detail',
    ),
]
