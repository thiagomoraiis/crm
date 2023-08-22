from ..models import Product
from .serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


class ProductModelViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)
