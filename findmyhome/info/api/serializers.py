from rest_framework import serializers
from info.models import HomeAds


class HomeAdsSerializer(serializers.ModelSerializer):    
    class Meta:
        model = HomeAds
        fields = "__all__"
