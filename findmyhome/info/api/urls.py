from django.contrib import admin
from django.urls import path
from info.api import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("houses/", views.HomeAdsListCreateAPIView.as_view(), name='home-list'),
    path("house/<int:pk>", views.HomeAdsDetailAPIView.as_view(), name='home-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])
