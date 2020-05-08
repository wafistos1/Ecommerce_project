from django.urls import path
from annonce import views
from .views import AnnonceDetailView, annonceListView, annonceUpdateView

urlpatterns = [

    path('', views.home, name='home'),
    path('annonce/add', views.add_annonce, name='add_annonce'),
    path('annonce/detail/<uuid:pk>', AnnonceDetailView.as_view(), name='annonce_detail'),
    path('annonce/list', annonceListView.as_view(), name='annonce_list'),
    path('annonce/update/<uuid:pk>', annonceUpdateView.as_view(), name='annonce_update'),
    path('annonce/update_image/<uuid:pk>', annonceUpdateImageView.as_view(), name='annonce_update_image'),
    ]