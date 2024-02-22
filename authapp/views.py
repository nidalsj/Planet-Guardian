from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def signupuser(request):
    if request.method=='POST':
        fullname=request.POST.get("fullname")
        email=request.POST.get('email')
        phonenum=request.POST.get("phonenum")
        password=request.POST.get("pass1")
        repassword=request.POST.get("pass2")

        #password length
        if len(password)<8:
            messages.error(request,'Password is too short')
            return render(request,'signup.html')

        #email and password are the same
        if email==password:
            messages.error(request,'Email and password cannot be the same')
            return render(request,'signup.html')

        #email or phone number already exists
        if User.objects.filter(email=email).exists() or User.objects.filter(username=phonenum).exists():
            messages.error(request,'Email or phone number already exists')
            return render(request,'signup.html')

        #passwords match
        if password!=repassword:
            messages.error(request,'Passwords do not match')
            return render(request,'signup.html')

        #phone number length
        if len(phonenum)!=10:
            messages.error(request,'Phone number should be 10 digits')
            return render(request,'signup.html')

        #phone number is same as the password
        if phonenum==password:
            messages.error(request,'Phone number cannot be your password')
            return render(request,'signup.html')

        #create a new user using Django User model
        user = User.objects.create_user(username=phonenum, password=password, email=email, first_name=fullname)

        messages.success(request,'Account created. Please log in')
        return render(request,'login.html')
    else:
        return render(request,'signup.html')


def loginuser(request):
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")

        # Check if the user exists
        user=authenticate(request, username=username, password=password)

        if user is not None:
            # Log in the user
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'You need to signup first')
            return render(request,'login.html')
    else:
        return render(request,'login.html')
    

def logout_user(request):
    logout(request)
    return redirect('home')

