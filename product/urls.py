from django.urls import path # noqa
from .api.views import product_api_list, product_api_detail
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
        '',
        ProductListView.as_view(),
        name='product-list'
    ),
    path(
        '<slug:slug>/',
        ProductDetailView.as_view(),
        name='product-detail',
    ),
    path(
        'api/v1/',
        product_api_list,
        name='product-api-list'
    ),
    path(
        'api/v1/<int:id>/',
        product_api_detail,
        name='product-api-detail'
    )
]
