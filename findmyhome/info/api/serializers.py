from rest_framework import serializers
from info.models import RentalHouse, OnSaleHouse



class OnSaleHouseSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OnSaleHouse
        fields = '__all__'
        
    
class RentalHouseSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RentalHouse
        fields = '__all__'