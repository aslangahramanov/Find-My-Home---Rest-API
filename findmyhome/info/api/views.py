from rest_framework import generics
from info.models import HomeAds
from info.api.serializers import HomeAdsSerializer
from info.api.pagination import MyPagination
from django_filters.rest_framework import DjangoFilterBackend




        
class HomeAdsListCreateAPIView(generics.ListCreateAPIView):
    # queryset = HomeAds.objects.all()
    serializer_class = HomeAdsSerializer
    pagination_class = MyPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'rooms', 'price', 'buy_or_rent', 'currency']
    
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




class HomeAdsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HomeAds.objects.all()
    serializer_class = HomeAdsSerializer
    