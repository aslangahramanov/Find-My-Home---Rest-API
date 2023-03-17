from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from info.models import HomeAds
from info.api.serializers import HomeAdsSerializer



@api_view(['GET', 'POST'])

def home_ads_create_api_view(request):
    if request.method == 'GET':
        homes = HomeAds.objects.all()
        serializer = HomeAdsSerializer(homes, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        if request.data:
            serializer = HomeAdsSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
        return Response(status = status.HTTP_204_NO_CONTENT)
        