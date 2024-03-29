from django.urls import path
from homework_rest.views import list_create, detail_fruits, fruits_list
from homework_rest.views import (
    fruits_list,
    fruits_create,
    fruits_delete,
    fruits_update,
    fruits_patrial_update
)
urlpatterns = [
    path('lists/', list_create),
    path('detail_fruit/<int:pk>', detail_fruits),
    path('fruits/', fruits_list),
    path('fruits/<int:pk>/', fruits_list),
    path('fruits/create/', fruits_create),
    path('fruits/update/<int:pk>/', fruits_update),
    path('fruits/pr-update/<int:pk>/', fruits_patrial_update),
    path('fruits/delete/<int:pk>/', fruits_delete)
]

