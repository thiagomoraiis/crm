from django.views.generic import ListView
from cart.models import Cart, CartItem


class CartListView(ListView):
    template_name = 'cart/pages/cart.html'
    context_object_name = 'products'
    model = CartItem

    def get_queryset(self):
        user_cart = Cart.objects.get(cart_owner=self.request.user)
        cart_item = CartItem.objects.filter(cart=user_cart)
        return cart_item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quantity'] = self.get_queryset().count()
        return context
