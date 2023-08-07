from django.urls import path
from .views import IndexListView, DashboardTemplateView, ProductDetailView


app_name = 'core'

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('dashboard/', DashboardTemplateView.as_view(), name='dashboard'),
    path('product/<slug:slug>/', ProductDetailView.as_view())
]
