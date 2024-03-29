from django.contrib import admin

from homework_rest.models import Fruits


@admin.register(Fruits)
class FruitsAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
