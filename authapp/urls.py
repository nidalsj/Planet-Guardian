from django.urls import path
from django.conf import settings
from . import views


urlpatterns = [
    path('signup', views.signupuser, name='signup'),
    path('login', views.loginuser, name='login'),
    path('logout', views.logout_user, name='logout'),
    
]
