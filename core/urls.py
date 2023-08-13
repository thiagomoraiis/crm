from django.urls import path
from .views import (IndexListView, DashboardTemplateView,
                    RegisterTemplateView, ProductListView,
                    TransactionsListView)
from product.views import (ProductDetailView, ProductCreateView,
                           ProductUpdateView, ProductDeleteView)
from cart.views import CartView, remove_item


app_name = 'core'

urlpatterns = [
    path(
        '',
        IndexListView.as_view(),
        name='index'
    ),
    path(
        'dashboard/',
        DashboardTemplateView.as_view(),
        name='dashboard'
    ),
    path(
        'product/<slug:slug>/',
        ProductDetailView.as_view(),
        name='product-detail',
    ),
    path(
        'register/',
        RegisterTemplateView.as_view(),
        name='register'
    ),
    path(
        'product-form/create/',
        ProductCreateView.as_view(),
        name='product-create'),
    path(
        'product-form/update/<slug:slug>/',
        ProductUpdateView.as_view(),
        name='product-update'
    ),
    path(
        'product-form/delete/<slug:slug>/',
        ProductDeleteView.as_view(),
        name='product-delete'
    ),
    path(
        'list/',
        ProductListView.as_view(),
        name='product-list'
    ),
    path(
        'cart/',
        CartView.as_view(),
        name='cart'
    ),
    path(
        'cart/remove/<int:id>/',
        remove_item,
        name='remove-cart'
    ),
    path(
        'transactions/',
        TransactionsListView.as_view(),
        name='transactions'
    )
]
