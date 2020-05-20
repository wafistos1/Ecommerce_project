from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import search 


urlpatterns = [
     path('search/', search, name='search'),

]

