from django.urls import path
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
]
