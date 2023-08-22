from .serializers import InventorySerializer, InvoicingSerializer
from ..models import Inventory, Invoicing
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView


class InventoryModelViewSet(ModelViewSet):
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        qs = super().get_queryset()
        qs.select_related('product')
        return qs


class InvoicingListAPIView(ListAPIView):
    serializer_class = InvoicingSerializer
    queryset = Invoicing.objects.all()
