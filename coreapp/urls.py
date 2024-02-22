from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('gallery', views.imagegallery,name='gallery'),
    path('contact', views.contactadmin,name='contact'),
    path('blogs', views.readblogs,name='blogs'),

]
