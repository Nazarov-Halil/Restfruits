from rest_framework import serializers

from rest_homework_2.models import Fruits


class FruitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruits
        fields = (
            'id',
            'title',
            'price'
        )
