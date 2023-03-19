import django_filters

from info.models import HomeAds


class PriceFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = HomeAds
        fields = ['min_price', 'max_price']