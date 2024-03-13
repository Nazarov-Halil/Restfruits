from django.contrib import admin

from rest_homework_2.models import Fruits


@admin.register(Fruits)
class FruitsAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
