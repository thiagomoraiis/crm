# from django.shortcuts import render, get_object_or_404
# from django.views.generic import View
# from .models import Cart, CartItem
# from product.models import Product
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator


# class ProductDetailView(View):
#     def get_product(self, request, slug):
#         product = get_object_or_404(
#             Product, slug=slug
#         )
#         return product
#
#     @method_decorator(login_required, name='post')
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
#
#     def get(self, request, slug):
#         product = self.get_product()
#         context = {'product': product}
#         return render(request, 'core/pages/product.html', context)
#
#     def post(self, request, slug):
#         product = self.get_product()
#         quantity = int(self.request.POST.get('quantity', 0))
#         cart, created = Cart.objects.get_or_create(
#             cart_owner=self.request.user, status='open',
#         )
#         item_cart, created = CartItem.objects.get_or_create(
#             product_item=product, cart=cart,
#             quantity=quantity, defaults={'total_cart_item': 0}
#         )
#
#         product.stock -= quantity
#
#         product.save()
#         item_cart.save()
#         return render(request, 'core/pages/product.html',
#           {'product': product})

# class ProductDetailView(DetailView):
#     template_name = 'core/pages/product.html'
#     model = Product
#     context_object_name = 'product'
#     slug_field = 'slug'
#     slug_url_kwarg = 'slug'
