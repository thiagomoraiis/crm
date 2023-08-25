from ..models import Product
from .serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from core.models import Inventory
from django.shortcuts import get_object_or_404


class ProductModelViewSet(ModelViewSet):
    """
    A Model ViewSet responsible for handling CRUD operations
    on the Product model.

    Attributes:
        serializer_class: The serializer class to use for
            serialization and deserialization.
        queryset: The queryset of products.
        lookup_field: The field used for looking up individual products.
        lookup_url_kwarg: The keyword argument used to retrieve the
            lookup field from the URL.
        permission_classes: The permission classes to apply to the view.

    Methods:
        get_queryset(): Retrieves the queryset of products.
        create(request, *args, **kwargs): Creates a new product and
            associates it with the current user.
        retrieve(request, *args, **kwargs): Retrieves the details
            of a specific product.
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs

    def create(self, request, *args, **kwargs):
        """
        Creates a new product and associates it with the current user.

        Args:
            request: The HTTP request.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: The response containing the serialized data
            of the created product.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(posted_by=self.request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieves the details of a specific product.

        Args:
            request: The HTTP request.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: The response containing the serialized product
            data and stock quantity if available.
        """
        product_id = self.kwargs.get('id')
        product = get_object_or_404(self.get_queryset(), id=product_id)
        serializer = ProductSerializer(instance=product)
        inventory = Inventory.objects.filter(product=product).first()

        if inventory:
            return Response(
                {**serializer.data, 'stock': inventory.quantity}
            )
        return Response(
            {'message': 'not found'}, status=status.HTTP_404_NOT_FOUND
        )


class ProductDetailAPIView(RetrieveAPIView):
    """
    A class-based API view responsible for retrieving details
    of a specific product.

    Attributes:
        queryset: The queryset of products.
        serializer_class: The serializer class used for serialization
        and deserialization.
        lookup_field: The field used for looking up individual products.

    Inheritance:
        RetrieveAPIView: Provides functionality for retrieving a single object.

    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
