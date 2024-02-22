from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('profile',views.myprofile,name='profile')
    
]
