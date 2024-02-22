from django.urls import path
from django.urls import reverse
from django.conf import settings
from . import views

urlpatterns = [
    path('biowaste/', views.biowaste, name='biowaste'),
    path('nonbiowaste/', views.nonbiowaste, name='nonbiowaste'),
    path('hazardous/', views.hazardouswaste, name='hazardous'),
    path('payment/<str:wastetype>/<int:weight>/', views.paymentview, name='payment'),
]

