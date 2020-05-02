from django.urls import path
from annonce import views

urlpatterns = [
    path('annonce/add', views.add_annonce, name='add_annonce'),
    path('annonce/detail', views.annonce_detail, name='annonce_detail'),
    ]