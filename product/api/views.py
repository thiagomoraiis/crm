from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from ..models import Product
from .serializers import ProductModelSerializer
from rest_framework import status # noqa


@api_view(['GET'])
def product_api_list(request):
    products = Product.objects.all()[0:11].\
        prefetch_related('tags')
    serializer = ProductModelSerializer(
        instance=products, many=True,
        context={'request': request},
    )
    return Response(serializer.data)


@api_view(['POST'])
def product_api_create(request):
    serializer = ProductModelSerializer(
        data=request.data, context={'request': request}
    )

    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def product_api_detail(request, id):
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


@api_view(['PUT'])
def product_api_update(request, id):
    product = get_object_or_404(
        Product.objects.filter(id=id), id=id
    )
    serializer = ProductModelSerializer(
        instance=product, data=request.data
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['DELETE'])
def product_api_delete(request, id):
    product = get_object_or_404(
        Product.objects.filter(id=id),
        id=id
    )
    product.delete()
    return Response(
        status=status.HTTP_204_NO_CONTENT,
    )
