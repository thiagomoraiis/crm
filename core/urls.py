from django.urls import path
from .api.views import (InventoryListAPIView, InventoryRetrieveAPIView,
                        InventoryCreateAPIView, InventoryUpdateAPIView,
                        InventoryDestroyAPIView, InvoicingListAPIView)
from .views import (IndexListView, DashboardTemplateView,
                    TransactionsListView, InventoryCreateView,
                    InventoryUpdateView, InventoryDeleteView,
                    InventoryListView)


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
        InventoryListAPIView.as_view(),
        name='inventory-api-list'
    ),
    path(
        'inventory/api/v1/create/',
        InventoryCreateAPIView.as_view(),
        name='inventory-api-create'
    ),
    path(
        'inventory/api/v1/detail/<int:id>/',
        InventoryRetrieveAPIView.as_view(),
        name='inventory-api-detail'
    ),
    path(
        'inventory/api/v1/update/<int:id>/',
        InventoryUpdateAPIView.as_view(),
        name='inventory-api-update',
    ),
    path(
        'inventory/api/v1/delete/<int:id>/',
        InventoryDestroyAPIView.as_view(),
        name='inventory-api-delete'
    ),
    path(
        'invoicing/api/v1/',
        InvoicingListAPIView.as_view(),
        name='invoicing-api-list'
    )
]
