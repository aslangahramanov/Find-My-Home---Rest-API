from django.contrib import admin
from django.urls import path
from info.api import views as api_views

urlpatterns = [
    path("homes/", api_views.home_ads_create_api_view, name='homes')
]
