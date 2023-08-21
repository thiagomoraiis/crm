from ..models import Product
from .serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet


class ProductModelViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs
