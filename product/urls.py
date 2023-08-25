from django.urls import path
from .api.views import ProductModelViewSet
from .views import (ProductCreateView, ProductDetailView, ProductUpdateView,
                    ProductListView, ProductDeleteView, )

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

    # API

    path(
        'api/v1/',
        ProductModelViewSet.as_view({'get': 'list'}),
        name='product-api-list'
    ),
    path(
        'api/v1/detail/<int:id>/',
        ProductModelViewSet.as_view({'get': 'retrieve'}),
        name='product-api-detail',
    ),
    path(
        'api/v1/create/',
        ProductModelViewSet.as_view({'post': 'create'}),
        name='product-api-create',
    ),
    path(
        'api/v1/update/<int:id>/',
        ProductModelViewSet.as_view({'put': 'update'}),
        name='product-api-update',
    ),
    path(
        'api/v1/delete/<int:id>/',
        ProductModelViewSet.as_view({'delete': 'destroy'}),
        name='product-api-delete'
    ),
    # path(
    #     'api/v1/detail/<int:id>/',
    #     ProductDetailAPIView.as_view(),
    #     name='product-api-detail',
    # ),
]
