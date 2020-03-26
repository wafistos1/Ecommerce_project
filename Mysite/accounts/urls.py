from django.urls import path
from accounts import views  
from django.conf import settings
from django.conf.urls.static import static

# Mettre ca temporairement ( )
urlpatterns = [
path('', views.home, name='home'),
]
