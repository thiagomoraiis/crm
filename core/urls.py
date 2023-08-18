from django.urls import path
from .api.views import (inventory_api_create_item, inventory_api_delete_item,
                        inventory_api_detail_item, inventory_api_list,
                        inventory_api_update_item)
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
        inventory_api_list,
        name='inventory-api-list'
    ),
    path(
        'inventory/api/v1/create/',
        inventory_api_create_item,
        name='inventory-api-create'
    ),
    path(
        'inventory/api/v1/detail/<int:id>/',
        inventory_api_detail_item,
        name='inventory-api-detail'
    ),
    path(
        'inventory/api/v1/update/<int:id>/',
        inventory_api_update_item,
        name='inventory-api-update',
    ),
    path(
        'inventory/api/v1/delete/<int:id>/',
        inventory_api_delete_item,
        name='inventory-api-delete'
    )
]
