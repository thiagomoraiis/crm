from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from cart.models import Cart, CartItem
from product.models import Product
from django.views.generic import (DeleteView, View,
                                  CreateView, UpdateView, ListView)


class ProductDetailView(View):
    """
    A class-based view to display product details and add products to
        the shopping cart.

    Only logged-in users can add products to the cart.

    Methods:
        get_product(request, slug): Retrieves the product using its slug
            from the database.
        dispatch(request, *args, **kwargs): Ensures that only authenticated
            users can access the view.
        get(request, slug): Handles HTTP GET requests and renders the product
            details page.
        post(request, slug): Handles HTTP POST requests and adds the product
            to the cart.
        update_or_create_item_product(cart, product, quantity): Updates or
            creates a cart item for the product.
    """

    def get_product(self, request, slug):
        """
        Retrieves a product using its slug from the database.

        Args:
            request: The HTTP request.
            slug: The slug of the product.

        Returns:
            Product: The retrieved product.
        """
        product = get_object_or_404(
            Product, slug=slug
        )
        return product

    @method_decorator(login_required, name='post')
    def dispatch(self, request, *args, **kwargs):
        """
        Ensures that only authenticated users can access the view.

        Args:
            request: The HTTP request.
            args: Additional arguments.
            kwargs: Additional keyword arguments.

        Returns:
            HttpResponse: The response.
        """
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, slug):
        """
        Handles HTTP GET requests and renders the product details page.

        Args:
            request: The HTTP request.
            slug: The slug of the product.

        Returns:
            HttpResponse: The rendered response.
        """
        product = self.get_product(request, slug)
        context = {'product': product}
        return render(request, 'product/pages/product.html', context)

    def post(self, request, slug):
        """
        Handles HTTP POST requests and adds the product to the cart.

        Args:
            request: The HTTP request.
            slug: The slug of the product.

        Returns:
            HttpResponse: The rendered response.
        """
        product = self.get_product(request, slug)
        quantity = int(self.request.POST.get('quantity', ''))
        cart, created = Cart.objects.get_or_create(
            cart_owner=self.request.user
        )

        self.update_or_create_item_product(cart, product, quantity)

        return render(
            request, 'product/pages/product.html',
            {'product': product}
        )

    def update_or_create_item_product(self, cart, product, quantity):
        """
        Updates or creates a cart item for the product.

        Args:
            cart: The cart object.
            product: The product to add to the cart.
            quantity: The quantity of the product.

        Returns:
            None
        """
        item_cart = CartItem.objects.filter(
            product_item=product, cart=cart
        ).first()

        if item_cart:
            item_cart.quantity += quantity
            item_cart.total_price_item = \
                item_cart.quantity * item_cart.product_item.price
            item_cart.save()
        else:
            item_cart = CartItem.objects.create(
                product_item=product, cart=cart,
                quantity=quantity
            )


class ProductCreateView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    """
    A Class-Based View (CBV) responsible for creating a new product.

    Requires the user to be authenticated and a superuser to access the view.

    Attributes:
        template_name (str): The name of the template used for rendering.
        fields (list): A list of fields in the creation form.
        model (Model): The model associated with the view.
        success_url (str): The URL to redirect to after successful creation.

    Methods:
        form_valid(form): Executed when the form is valid.
        test_func(): Checks if the user is a superuser.

    Inheritance:
        UserPassesTestMixin: Provides custom permission checking.
        LoginRequiredMixin: Requires the user to be authenticated.
        CreateView: Provides object creation functionality.

    """
    template_name = 'product/pages/product_form.html'
    fields = [
        'name', 'price', 'description',
        'image', 'category',
    ]
    model = Product
    success_url = reverse_lazy('product:product-list')

    def form_valid(self, form):
        """
        Executed when the form is valid.

        Sets the user who posted as the current authenticated user.

        Args:
            form (ModelForm): The form filled by the user.

        Returns:
            HttpResponse: The rendered response.
        """
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
        Checks if the user is a superuser.

        Returns:
            bool: True if the user is a superuser, False otherwise.
        """
        return self.request.user.is_superuser


class ProductUpdateView(UserPassesTestMixin, UpdateView):
    """
    A Class-Based View (CBV) responsible for updating an existing product.

    Requires the user to be a superuser to access the view.

    Attributes:
        template_name (str): The name of the template used for rendering.
        fields (list): A list of fields in the update form.
        model (Model): The model associated with the view.
        context_object_name (str): The name of the variable used to pass
            the product object to the template.
        slug_field (str): The name of the field used as the slug.
        slug_url_kwarg (str): The keyword argument for the slug in the URL.
        success_url (str): The URL to redirect to after successful update.

    Methods:
        test_func(): Checks if the user is a superuser.

    Inheritance:
        UserPassesTestMixin: Provides custom permission checking.
        UpdateView: Provides object update functionality.

    """
    template_name = 'product/pages/product_form.html'
    fields = [
        'name', 'price', 'description',
        'image', 'category',
    ]
    model = Product
    context_object_name = 'product'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('product:product-list')

    def test_func(self):
        """
        Checks if the user is a superuser.

        Returns:
            bool: True if the user is a superuser, False otherwise.
        """
        return self.request.user.is_superuser


class ProductDeleteView(UserPassesTestMixin, DeleteView):
    """
    A Class-Based View (CBV) responsible for deleting an existing product.

    Requires the user to be a superuser to access the view.

    Attributes:
        model (Model): The model associated with the view.
        template_name (str): The name of the template used for rendering.
        success_url (str): The URL to redirect to after successful deletion.
        context_object_name (str): The name of the variable used to pass the
            product object to the template.
        slug_field (str): The name of the field used as the slug.
        slug_url_kwarg (str): The keyword argument for the slug in the URL.

    Methods:
        test_func(): Checks if the user is a superuser.

    Inheritance:
        UserPassesTestMixin: Provides custom permission checking.
        DeleteView: Provides object deletion functionality.

    """
    model = Product
    template_name = 'product/pages/product_delete.html'
    success_url = reverse_lazy('product:product-list')
    context_object_name = 'product'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def test_func(self):
        """
        Checks if the user is a superuser.

        Returns:
            bool: True if the user is a superuser, False otherwise.
        """
        return self.request.user.is_superuser


class ProductListView(UserPassesTestMixin, ListView):
    """
    A Class-Based View (CBV) responsible for listing products.

    Requires the user to be a superuser to access the view.

    Attributes:
        template_name (str): The name of the template used for rendering.
        context_object_name (str): The name of the variable used to pass
            the list of products to the template.
        queryset (QuerySet): The queryset of products to be displayed.
        paginate_by (int): The number of products displayed per page.

    Methods:
        get_queryset(): Retrieves the queryset of products and performs
            additional customization.
        test_func(): Checks if the user is a superuser.

    Inheritance:
        UserPassesTestMixin: Provides custom permission checking.
        ListView: Provides a list view for displaying a collection of objects.

    """
    template_name = 'product/pages/list_products.html'
    context_object_name = 'products'
    queryset = Product.objects.all()
    paginate_by = 12

    def get_queryset(self):
        """
        Retrieves the queryset of products and performs additional
            customization.

        Returns:
            QuerySet: The customized queryset of products.
        """
        qs = super().get_queryset()
        qs = qs.select_related('posted_by')
        return qs

    def test_func(self):
        return self.request.user.is_superuser
