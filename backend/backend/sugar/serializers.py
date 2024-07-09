from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Сarbohydrates


class СarbohydratesSerializer(ModelSerializer):

    class Meta:
        model = Сarbohydrates
        fields = ('id', 'cur_sugar', 'carbohydrate', 'cur_time')