from django.contrib import admin
from django.urls import path
from info.api import views

from rest_framework.urlpatterns import format_suffix_patterns

app_name = "api"



####        Endpoints used by the API. It converts the Api model views we have prepared into a 
###         view with the .as_view() method and enables them to open at the url we specified.
##          "houses/" for all data, "house/<pk>" for a single data by pk field.


urlpatterns = [
    path("houses/", views.HomeAdsListCreateAPIView.as_view(), name='house-list'),
    path("house/<int:pk>", views.HomeAdsDetailAPIView.as_view(), name='house-detail')
]



###  format_suffix_patterns shows the data in "Json" format by writing ".json" at the end of the url.
 


urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])
