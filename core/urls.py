from django.urls import path
from .views import (IndexListView, DashboardTemplateView,
                    ProductDetailView, RegisterTemplateView,
                    ProductCreateView, ProductUpdateView,
                    ProductDeleteView, ProductListView)


app_name = 'core'

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('dashboard/', DashboardTemplateView.as_view(), name='dashboard'),
    path('product/', ProductDetailView.as_view()),
    path('register/', RegisterTemplateView.as_view()),
    path('product-form/create/', ProductCreateView.as_view()),
    path('product-form/update/', ProductUpdateView.as_view()),
    path('product-form/delete/', ProductDeleteView.as_view()),
    path('list/', ProductListView.as_view())
]
