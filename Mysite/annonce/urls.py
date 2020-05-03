from django.urls import path
from annonce import views
from .views import AnnonceDetailView, annonceListView

urlpatterns = [
    path('annonce/add', views.add_annonce, name='add_annonce'),
    path('annonce/detail/<uuid:pk>', AnnonceDetailView.as_view(), name='annonce_detail'),
    path('annonce/list', annonceListView.as_view(), name='annonce_list'),
    ]