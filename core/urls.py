from django.urls import path
from .views import (IndexListView, DashboardTemplateView,
                    RegisterTemplateView, TransactionsListView)


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
        'register/',
        RegisterTemplateView.as_view(),
        name='register'
    ),
    path(
        'transactions/',
        TransactionsListView.as_view(),
        name='transactions'
    )
]
