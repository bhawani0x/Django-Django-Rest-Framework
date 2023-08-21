from django.contrib import admin
from django.urls import path, include
from . views import create_profile

urlpatterns = [
    path('create_profile/', create_profile, name='create_profile'),
    ]
