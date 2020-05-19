from django.urls import path
from annonce import views
from annonce.views import annonceListView, message_list, updateAnnonce, AnnonceDeletelView, add_annonce, annonceDetaiView, favorite, annonce_favorite_list, message_mp

urlpatterns = [
    path('', views.home, name='home'),
    path('annonce/add', views.add_annonce, name='add_annonce'),
    path('annonce/detail/<uuid:pk>', views.annonceDetaiView, name='annonce_detail'),
    path('annonce/favorite/<uuid:pk>', views.favorite, name='favorite_annonce'),
    path('annonce/favorite/', views.annonce_favorite_list, name='favorite_list'),
    path('annonce/message/<int:user_pk>', views.message_mp, name='message'),  
    path('annonce/messages/', views.message_list, name='message_list'),  
    # path('annonce/detail/<uuid:pk>', AnnonceDetailView.as_view(), name='annonce_detail'),
    path('annonce/list', annonceListView.as_view(), name='annonce_list'),
    path('annonce/delete/<uuid:pk>', AnnonceDeletelView.as_view(), name='annonce_delete'),
    path('annonce/update/<uuid:pk>', views.updateAnnonce, name='annonce_update'),
    ]