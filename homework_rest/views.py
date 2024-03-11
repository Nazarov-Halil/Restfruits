from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from homework_rest.serializer import FruitsSerializer

fruits_list = [
    {"id": 1, "name": "apple", "price": 60},
    {"id": 2, "name": "tangerine", "price": 90},
    {"id": 3, "name": "banana", "price": 70},
]



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
