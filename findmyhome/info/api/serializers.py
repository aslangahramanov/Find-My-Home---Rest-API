from rest_framework import serializers
from info.models import HomeAds


##     Our serializers file in the api folder. 
#      understandably an associated ModelSerializer class to serialize our model


class HomeAdsSerializer(serializers.ModelSerializer):    
    class Meta:
        model = HomeAds
        fields = "__all__"
