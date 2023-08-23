from django.urls import path
from .api.views import (
    BillingListAPIView,
    InventoryModelViewSet,
    RegisterAccountAPIView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from .views import (
    IndexListView, DashboardTemplateView,
    TransactionsListView, InventoryCreateView,
    InventoryUpdateView, InventoryDeleteView,
    InventoryListView
)


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
        'transactions/',
        TransactionsListView.as_view(),
        name='transactions'
    ),
    path(
        'inventory/',
        InventoryListView.as_view(),
        name='inventory-list'
    ),
    path(
        'inventory/create/',
        InventoryCreateView.as_view(),
        name='inventory-create'
    ),
    path(
        'inventory/update/<int:id>/',
        InventoryUpdateView.as_view(),
        name='inventory-update'
    ),
    path(
        'inventory/delete/<int:id>/',
        InventoryDeleteView.as_view(),
        name='inventory-delete'
    ),

    # api

    path(
        'inventory/api/v1/',
        InventoryModelViewSet.as_view({'get': 'list'}),
        name='inventory-api-list'
    ),
    path(
        'inventory/api/v1/create/',
        InventoryModelViewSet.as_view({'post': 'create'}),
        name='inventory-api-create'
    ),
    path(
        'inventory/api/v1/detail/<int:id>/',
        InventoryModelViewSet.as_view({'get': 'retrieve'}),
        name='inventory-api-detail'
    ),
    path(
        'inventory/api/v1/update/<int:id>/',
        InventoryModelViewSet.as_view({'put': 'update'}),
        name='inventory-api-update',
    ),
    path(
        'inventory/api/v1/delete/<int:id>/',
        InventoryModelViewSet.as_view({'delete': 'destroy'}),
        name='inventory-api-delete'
    ),
    path(
        'billing/api/v1/',
        BillingListAPIView.as_view({'get': 'list'}),
        name='billing-api-list'
    ),

    # Login

    path(
        'user/api/register/',
        RegisterAccountAPIView.as_view(),
    ),
    path(
        'user/api/login/token/',
        TokenObtainPairView.as_view()
    ),
    path(
        'user/api/login/token/refresh/',
        TokenRefreshView.as_view()
    ),
    path(
        'user/api/login/token/verify/',
        TokenVerifyView.as_view()
    )
]
