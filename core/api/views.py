from rest_framework.response import Response
from rest_framework import status
from ..models import Inventory, Company
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
from .permissions import IsOwner
from .serializers import (InventorySerializer, CompanySerializer,
                          UserSerializer)


class InventoryModelViewSet(ModelViewSet):
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        qs = super().get_queryset()
        qs.select_related('product')
        return qs


class CompanyModelViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_object(self):
        pk = self.kwargs.get('pk', '')

        obj = get_object_or_404(
            self.get_queryset(), pk=pk
        )

        self.check_object_permissions(self.request, obj)

        return obj


class RegisterAccountAPIView(APIView):
    http_method_names = ['post']

    def post(self, request):
        serializer = UserSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user_exists = User.objects.filter(username=username).exists()
        if not user_exists:
            serializer.save(password=make_password(password))
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )

        return Response(
            {'message': 'a user with that name already exists'},
            status=status.HTTP_400_BAD_REQUEST
        )
