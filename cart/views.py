from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
from cart.models import Cart, CartItem
from core.models import Company, Transactions, Inventory
from customer.models import PurchaseHistoric, HistoricItem


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
                products = products.select_related('product_item', 'cart')
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
            )

    def post(self, request):
        product_cart = self.get_products(request)
        total_price_cart = product_cart.aggregate(
            total_price_sum=Sum('total_price_item'))['total_price_sum']

        self.create_or_update_billing(total_price_cart)
        self.create_historic_item(product_cart)
        self.update_stock_view(product_cart)

        product_cart.delete()

        return render(
            request, 'cart/pages/cart.html',
            {'products': product_cart,
             'quantity': product_cart.count()
             }
        )

    def create_historic_item(self, product_cart):
        historic, created = PurchaseHistoric.objects.get_or_create(
            owner=self.request.user
        )
        for cart_item in product_cart:
            historic_item = HistoricItem.objects.create( # noqa
                historic=historic, product=cart_item.product_item
            )

    def create_or_update_billing(self, total_price_cart):
        transactions = self.create_transaction(total_price_cart)
        billing = Company.objects.filter().first()

        if billing:
            billing.total_value += transactions.value
            billing.save()
        else:
            value_billing = transactions.value
            billing = Company.objects.create(total_value=value_billing)

    def create_transaction(self, total_price_cart):
        transactions = Transactions.objects.create( # noqa
            value=total_price_cart, client=self.request.user
        )
        return transactions

    def update_stock_view(self, product_cart):
        for item in product_cart:
            item_filter = item.product_item.name
            item_quantity = item.quantity

            inventory_item = Inventory.objects.filter(
                product__name=item_filter
            ).first()

            if inventory_item:
                inventory_item.quantity -= item_quantity
                inventory_item.save()
            else:
                raise ObjectDoesNotExist


def remove_item(request, id):
    product = get_object_or_404(CartItem, id=id)
    product.delete()
    return redirect('core:index')
