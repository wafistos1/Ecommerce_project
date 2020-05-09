from django.urls import path
from annonce import views
from .views import AnnonceDetailView, annonceListView, updateAnnonce, AnnonceDeletelView

urlpatterns = [
    path('', views.home, name='home'),
    path('annonce/add', views.add_annonce, name='add_annonce'),
    path('annonce/detail/<uuid:pk>', AnnonceDetailView.as_view(), name='annonce_detail'),
    path('annonce/list', annonceListView.as_view(), name='annonce_list'),
    path('annonce/delete/<uuid:pk>', AnnonceDeletelView.as_view(), name='annonce_delete'),
    path('annonce/update/<uuid:pk>', views.updateAnnonce, name='annonce_update'),
    ]