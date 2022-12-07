from django.contrib import admin
from django.urls import path, include
from .views import Download_codes, index

urlpatterns = [
    path("", index, name='index'),
    path("download-codes/", Download_codes.my_view, name='down'),
]