from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

# Mettre ca temporairement ( )
urlpatterns = [
path('', views.home, name='home'),

# path('login/', auth_views.LoginView.as_view(template_name='register/login.html'), name='login'),
# path('logout/', auth_views.LogoutView.as_view(template_name='register/logout.html'), name='logout'),

path('accounts/user', views.register, name='register'),

]
