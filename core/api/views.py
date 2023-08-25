from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
from ..models import Inventory, Company
from .permissions import IsOwner
from .serializers import (InventorySerializer, CompanySerializer,
                          UserSerializer)


class InventoryModelViewSet(ModelViewSet):
    """
    A class-based viewset that provides CRUD operations for Inventory objects.

    Attributes:
    serializer_class (Serializer): The serializer class to use for
    Inventory objects.
    queryset (QuerySet): The queryset containing the list of Inventory objects.
    lookup_field (str): The field to use as the lookup for individual
    object retrieval.
    lookup_url_kwarg (str): The URL keyword argument name for the
    lookup field.
    """
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        """
        Retrieves the queryset of Inventory objects and performs a
        select_related operation to fetch associated products efficiently.

        Returns:
        QuerySet: The queryset of Inventory objects with associated
        products.
        """
        qs = super().get_queryset()
        qs.select_related('product')
        return qs


class CompanyModelViewSet(ModelViewSet):
    """
    A class-based viewset that provides CRUD operations for Company objects.

    Attributes:
    queryset (QuerySet): The queryset containing the list of
    Company objects.
    serializer_class (Serializer): The serializer class to
    use for Company objects.
    permission_classes (list): The list of permission classes
    applied to this viewset.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_object(self):
        """
        Retrieves a specific Company object based on the
        provided primary key.

        Returns:
        Company: The retrieved Company object.

        Raises:
        Http404: If the Company object with the provided
        primary key is not found.
        """
        pk = self.kwargs.get('pk', '')
        obj = get_object_or_404(
            self.get_queryset(), pk=pk
        )

        self.check_object_permissions(self.request, obj)
        return obj


class RegisterAccountAPIView(APIView):
    """
    A class-based API view for registering user accounts.

    Attributes:
    http_method_names (list): The list of allowed HTTP methods for this view.
    """
    http_method_names = ['post']

    def post(self, request):
        """
        Handles the HTTP POST request to create a new user account.

        Args:
        request (HttpRequest): The HTTP request object.

        Returns:
        Response: A response indicating the success or failure of
        the user account registration.
        """
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
