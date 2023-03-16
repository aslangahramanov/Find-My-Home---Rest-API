from rest_framework import serializers
from info.models import HomeAds


class HomeAdsSerializer(serializers.Serializer):
        id = serializers.IntegerField(read_only=True)
        title = serializers.CharField()
        description = serializers.CharField()
        price = serializers.CharField()
        currency = serializers.CharField()
        square_price = serializers.CharField()
        category = serializers.CharField()
        floor = serializers.CharField()
        area = serializers.CharField()
        rooms = serializers.CharField()
        no = serializers.CharField()

        def create(self, validated_data):
            return HomeAds.objects.create(**validated_data)
        
        def update(self, instance, validated_data):
            instance.title = validated_data.get("title", instance.title)
            instance.description = validated_data.get("description", instance.description)
            instance.price = validated_data.get("price", instance.price)
            instance.currency = validated_data.get("currency", instance.currency)
            instance.square_price= validated_data.get("square_price", instance.square_price)
            instance.category = validated_data.get("category", instance.category)
            instance.floor = validated_data.get("floor", instance.floor)
            instance.area = validated_data.get("area", instance.area)
            instance.rooms = validated_data.get("rooms", instance.rooms)
            instance.no = validated_data.get("no", instance.no)
            instance.save()
            return instance