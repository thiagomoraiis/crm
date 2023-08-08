from django.urls import path
from .views import (IndexListView, DashboardTemplateView,
                    RegisterTemplateView, ProductListView)
from product.views import (ProductDetailView, ProductCreateView,
                           ProductUpdateView, ProductDeleteView)
from cart.views import CartListView


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
        CartListView.as_view(),
        name='cart'
    )
]
