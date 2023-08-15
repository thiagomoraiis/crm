from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from cart.models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
from core.models import Invoicing, Transactions
from customer.models import PurchaseHistoric, HistoricItem
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required


class CartView(View):
    def get_products(self, request):
        if self.request.user.is_authenticated:
            try:
                cart = Cart.objects.filter(
                    cart_owner=self.request.user
                ).first()
                products = CartItem.objects.filter(
                    cart=cart
                )
                return products

            except ObjectDoesNotExist:
                return CartItem.objects.none()

    def get(self, request):
        product_cart = self.get_products(request)
        if product_cart:
            total_price_cart = product_cart.aggregate(
                total_price_sum=Sum('total_price_item')
            )['total_price_sum']

            return render(
                request, 'cart/pages/cart.html',
                {'products': product_cart,
                 'quantity': product_cart.count(),
                 'total_price_cart': round(total_price_cart, 2),
                 }
            )
        else:
            return render(
                request, 'cart/pages/cart.html',
                {'product_cart': product_cart}
            )

    def post(self, request):
        product_cart = self.get_products(request)
        total_price_cart = product_cart.aggregate(
            total_price_sum=Sum('total_price_item')
        )['total_price_sum']

        transactions = Transactions.objects.create( # noqa
            value=total_price_cart, client=self.request.user
        )
        invoicing = Invoicing.objects.filter().first()
        if invoicing:
            invoicing.total_value += transactions.value
            invoicing.save()
        else:
            value_invoicing = transactions.value
            invoicing = Invoicing.objects.create(total_value=value_invoicing)

        historic, created = PurchaseHistoric.objects.get_or_create(
            owner=self.request.user
        )
        for cart_item in product_cart:
            historic_item = HistoricItem.objects.create( # noqa
                historic=historic, product=cart_item.product_item
            )
        product_cart.delete()

        return render(
            request, 'cart/pages/cart.html',
            {'products': product_cart,
             'quantity': product_cart.count(),
             # 'total_price_cart': round(total_price_cart, 2),
             }
        )


def remove_item(request, id):
    product = get_object_or_404(CartItem, id=id)
    product.delete()
    return redirect('core:index')
