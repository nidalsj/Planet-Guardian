from django.shortcuts import render, redirect
from django.contrib import messages
from coreapp.models import Gallery,Contact, BlogPost
# Create your views here.

def index(request):
    return render(request,'home.html')

def imagegallery(request):
    posts=Gallery.objects.all().order_by('-timeStamp')
    context={"posts":posts}
    return render(request,'gallery.html',context)

def contactadmin(request):
    form_submitted = False
    if request.method=="POST":
        name=request.POST.get('fullname')
        usermail=request.POST.get('usermail')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        ctquery=Contact(name=name,email=usermail,subject=subject,description=message)
        ctquery.save()
        
        form_submitted = True
        messages.success(request, 'Your message has been submitted successfully!')
    return render(request,'contact.html', {'form_submitted': form_submitted})
        

def readblogs(request):
    blogs=BlogPost.objects.all().order_by('-timeStamp')
    blcontext={"blogs":blogs}
    return render(request,'blogspage.html',blcontext)

