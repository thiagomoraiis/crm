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
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs

    def create(self, request, *args, **kwargs):
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
        product_id = self.kwargs.get('id')
        product = get_object_or_404(
            self.get_queryset(), id=product_id
        )
        serializer = ProductSerializer(
            instance=product
        )
        inventory = Inventory.objects.filter(
            product=product
        ).first()

        if inventory:
            return Response(
                {**serializer.data, 'stock': inventory.quantity}
            )
        return Response(
            {'message': 'not found'}, status=status.HTTP_404_NOT_FOUND
        )


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
