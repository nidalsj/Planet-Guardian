from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def myprofile(request):
    return render(request,'profile.html')

