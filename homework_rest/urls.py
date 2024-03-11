from django.urls import path
from homework_rest.views import list_create, detail_fruits, fruits_list

urlpatterns = [
    path('lists/', list_create),
    path('detail_fruit/<int:pk>', detail_fruits),
]
