from django.contrib import admin
from django.urls import path, include
from info import views

app_name = "info"

urlpatterns = [
    path("", views.home, name="home")
]