from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import TestAAPIView

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken'))
]