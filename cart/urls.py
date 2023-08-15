from django.urls import path
from cart.views import CartView, remove_item

app_name = 'cart'

urlpatterns = [
    path(
        'cart/',
        CartView.as_view(),
        name='cart'
    ),
    path(
        'cart/remove/<int:id>/',
        remove_item,
        name='remove-cart'
    ),
]
