from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from ..models import Product
from .serializers import ProductModelSerializer
from rest_framework import status # noqa


@api_view(http_method_names=['GET', 'POST'])
def product_api_list(request):
    if request.method == 'GET':
        products = Product.objects.all()[0:11].\
            prefetch_related('tags')
        serializer = ProductModelSerializer(
            instance=products, many=True,
            context={'request': request},
        )
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def product_api_detail(request, id):
    if request.method == 'GET':
        product = get_object_or_404(
            Product.objects.filter(id=id),
            id=id
        )
        serializer = ProductModelSerializer(
            instance=product, many=False
        )
        return Response(
            serializer.data
        )
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        product = get_object_or_404(
            Product.objects.filter(id=id),
            id=id
        )
        product.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )
