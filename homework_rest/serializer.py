from rest_framework import serializers


class FruitsSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    price = serializers.IntegerField()


from rest_framework import serializers

from homework_rest.models import Fruits


class FruitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruits
        fields = (
            'id',
            'title',
            'price'
        )
