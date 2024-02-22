from django.shortcuts import render, redirect
from django.contrib import messages
from . models import BiowasteModel, NonbiowasteModel, HazardouswasteModel

# Create your views here.

def biowaste(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Please Login and Try Again')
        return redirect('login')
    
    if request.method == "POST":
        name = request.POST.get('username')
        wastetype_entered = request.POST.get('wastetype')
        weight_entered = request.POST.get('weight')
        phonenum = request.POST.get('phonenum')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        bioquery = BiowasteModel(name=name,
                                  wastetype=wastetype_entered,
                                  phonenum=phonenum,
                                  weight=weight_entered,
                                  address=address,
                                  city=city,
                                  state=state,
                                  pincode=pincode)
        bioquery.save()
        return redirect('payment', wastetype=wastetype_entered, weight=weight_entered)
    return render(request, 'bioform.html')


def nonbiowaste(request):
    if not request.user.is_authenticated:
        messages.warning(request,'Please Login and Try Again')
        return redirect('login')
    
    if request.method == "POST":
        name = request.POST.get('username')
        wastetype_entered = request.POST.get('wastetype')
        weight_entered = request.POST.get('weight')
        phonenum = request.POST.get('phonenum')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        nonbioquery = NonbiowasteModel(name=name,
                                  wastetype=wastetype_entered,
                                  phonenum=phonenum,
                                  weight=weight_entered,
                                  address=address,
                                  city=city,
                                  state=state,
                                  pincode=pincode)
        nonbioquery.save()
        return redirect('payment', wastetype=wastetype_entered, weight=weight_entered)
    return render(request,'nonbio.html')


def hazardouswaste(request):
    if not request.user.is_authenticated:
        messages.warning(request,'Please Login and Try Again')
        return redirect('login')
    
    if request.method == "POST":
        name = request.POST.get('username')
        wastetype_entered = request.POST.get('wastetype')
        weight_entered = request.POST.get('weight')
        phonenum = request.POST.get('phonenum')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        hazardbioquery = HazardouswasteModel(name=name,
                                  wastetype=wastetype_entered,
                                  phonenum=phonenum,
                                  weight=weight_entered,
                                  address=address,
                                  city=city,
                                  state=state,
                                  pincode=pincode)
        hazardbioquery.save()
        return redirect('payment', wastetype=wastetype_entered, weight=weight_entered)
    return render(request,'hazardous.html')


def paymentview(request, wastetype, weight):
    if not wastetype or not weight:
        return redirect('home')  #allows access to payment page only if form is submitted

    return render(request, 'paymentpage.html', {'wastetype': wastetype, 'weight': weight})

