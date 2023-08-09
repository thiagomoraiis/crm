from django.views.generic import ListView
from cart.models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist


class CartListView(ListView):
    template_name = 'cart/pages/cart.html'
    context_object_name = 'products'
    model = CartItem

    def get_queryset(self):
        if self.request.user.is_authenticated:
            try:
                cart = Cart.objects.get(
                    cart_owner=self.request.user
                )
                cart_items = CartItem.objects.filter(
                    cart=cart
                )
                return cart_items
            except ObjectDoesNotExist:
                return super().self.get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quantity'] = self.get_queryset().count()
        return context
