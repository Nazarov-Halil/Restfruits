from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from homework_rest.models import Fruits

from homework_rest.serializer import FruitsSerializer

fruits_list = [
    {"id": 1, "name": "apple", "price": 60},
    {"id": 2, "name": "tangerine", "price": 90},
    {"id": 3, "name": "banana", "price": 70},
]



# 1 Создание
@api_view(http_method_names=["GET", "POST"])
def list_create(request: Request):
    if request.method == 'POST':
        fruits_list.append(request.data)
        return Response(fruits_list, status=201)
    return Response(fruits_list, status=200)


@api_view(http_method_names=['GET'])
def detail_fruits(request: Request, pk: int):
    fruit = [i for i in fruits_list if i['id'] == pk]
    return Response(fruit, status=200)



# 2 Создание


@api_view(http_method_names=['GET'])
def fruits_list(request: Request, pk=None):
    if pk:
        data = Fruits.objects.get(pk=pk)
        serializer = FruitsSerializer(instance=data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    data = Fruits.objects.all()
    serializer = FruitsSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(http_method_names=['POST'])
def fruits_create(request:Request):
    title, price = request.data['title'], request.data['price']
    data = Fruits.objects.create(title=title, price=price)
    serializer = FruitsSerializer(instance=data)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(http_method_names=['PUT'])
def fruits_update(request: Request, pk):
    title, price = request.data['title'], request.data['price']

    data = Fruits.objects.get(id=pk)
    data.title = title
    data.price = price
    data.save()
    allfruits = Fruits.objects.all()
    serializer = FruitsSerializer(instance=allfruits, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(http_method_names=['PATCH'])
def fruits_patrial_update(request: Request, pk):
    try:
        title = request.data['title']
    except KeyError:
        title = None

    try:
        price = request.data['price']
    except KeyError:
        price = None

    data = Fruits.objects.get(id=pk)

    if title:
        data.title = title
        data.save()

    if price:
        data.price = price
        data.save()

    serializer = FruitsSerializer(instance=data)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(http_method_names=['DELETE'])
def fruits_delete(request: Request, pk):
    fruit = Fruits.objects.get(id=pk)
    fruit.delete()

    data = Fruits.objects.all()
    serializer = FruitsSerializer(instance=data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)