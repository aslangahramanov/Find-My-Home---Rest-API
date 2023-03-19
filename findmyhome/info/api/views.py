from rest_framework import generics
from info.models import HomeAds
from info.api.serializers import HomeAdsSerializer
from info.api.pagination import MyPagination
from django_filters.rest_framework import DjangoFilterBackend



####     Skins for the API. The "HomeAdsListCreateAPIView" we created using the generics
###      library helps us to list and generate data. The get and post methods are used here. 

        
class HomeAdsListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = HomeAdsSerializer
    pagination_class = MyPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'rooms', 'price', 'buy_or_rent', 'currency']
    
    
    


#####      We have to rewrite the get_queryset method for API Filtering. 
####       Here, we get the values given in the query_params that come with the request,
###        and when the values we get are not "None", we perform the filtering process. 
##         If we do filtering with more than one feature, we may need to use the "django-filter" library. 
#          After making the necessary adjustments, we can now enter more than one feature and filter. 

#          For example: "128.0.0.1:localhost/api/houses/?category=Yeni+tikli&rooms=3&min_price=500&max_price=1000"

    
    def get_queryset(self):
        queryset = HomeAds.objects.all()
        buy_or_rent = self.request.query_params.get('buy_or_rent')
        category = self.request.query_params.get('category')
        rooms = self.request.query_params.get('rooms')
        currency = self.request.query_params.get('currency')
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        
        
        if category is not None:
            queryset = queryset.filter(category=category)
        if rooms is not None:
            queryset = queryset.filter(rooms=rooms)
        if buy_or_rent is not None:
            queryset = queryset.filter(buy_or_rent=buy_or_rent)
        if currency is not None:
            queryset = queryset.filter(currency=currency)
        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)
        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)
            
        return queryset




####       "HomeAdsDetailAPIView" provides detailed usage as agreed on API data. 
###        The put, patch and delete methods we use here. 
##         However, you must specify which data you want to receive with pk.


class HomeAdsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HomeAds.objects.all()
    serializer_class = HomeAdsSerializer
    