from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import InventoryModelSerializer
from ..models import Inventory
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def inventory_api_list(request):
    inventory = Inventory.objects.all().\
        select_related('product')
    serializer = InventoryModelSerializer(
        intance=inventory, many=True,
        context={'request': request}
    )
    return Response(serializer.data)


@api_view(['GET'])
def inventory_api_detail_item(request, id):
    inventory_item = get_object_or_404(
        Inventory.objects.filter(id=id), id=id
    )
    serializer = InventoryModelSerializer(
        instance=inventory_item, many=False,
    )
    return Response(serializer.data)


@api_view(['POST'])
def inventory_api_create_item(request):
    serializer = InventoryModelSerializer(
        data=request.data, context={'request': request}
    )
    serializer.is_valid()
    serializer.save(raise_exception=True)
    return Response(serializer.data)


@api_view(['PUT'])
def inventory_api_update_item(request, id):
    inventory_item = get_object_or_404(
        Inventory.objects.filter(id=id), id=id
    )
    serializer = InventoryModelSerializer(
        instance=inventory_item, data=request.data,
    )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(
        serializer.errors, status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['DELETE'])
def inventory_api_delete_item(request, id=id):
    inventory_item = get_object_or_404(
        Inventory.objects.filter(id=id), id=id
    )
    inventory_item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
