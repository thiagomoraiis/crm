from .serializers import InventorySerializer, InvoicingSerializer
from ..models import Inventory, Invoicing
from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                     CreateAPIView, UpdateAPIView,
                                     DestroyAPIView)


class InventoryListAPIView(ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs.select_related('product')
        return qs


class InventoryRetrieveAPIView(RetrieveAPIView):
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


class InventoryCreateAPIView(CreateAPIView):
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()


class InventoryUpdateAPIView(UpdateAPIView):
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


class InventoryDestroyAPIView(DestroyAPIView):
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


class InvoicingListAPIView(ListAPIView):
    serializer_class = InvoicingSerializer
    queryset = Invoicing.objects.all()
