from django.shortcuts import render,redirect
from backend.models import *
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.hashers import make_password


# Create your views here.

def Home(request):
    
    
    data={
        'header_slider':Header_slider.objects.all(),
        'is_auther':request.user.is_authenticated,
        'new_products':Product.objects.all().order_by('-created_at'),
        'best_seller':Product.objects.all().order_by('selling_count'),
        'top_rate':Product.objects.all().order_by('selling_count','rating'),

    }



    return render(request, 'home/index.html' , data)


def Register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')

        if password !=confirm_password:
            return render(request, 'register/index.html',{'error':'Passwords do not match'})
        else:

            one_user=User.objects.filter(username=username).exists()

            if one_user:
                return redirect('/')
            else:
                User.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=make_password(password),
                is_superuser=0,
                is_staff=1,
                is_active=1
                
            )
            ones_user=authenticate(username=username, password=password)

            if ones_user:
                login(request,ones_user)
                return redirect('/')
            
    return render(request,'register/index.html')

def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')  
        else:
            
            return redirect('/register')

    return render(request, 'Login/index.html')


def Logout(request):
    logout(request)

    return redirect('/')

def Product_details(request, id):

    data={
        'one_prouduct':Product.objects.filter(id=id)
    }


    return render(request,'prouduct_details/index.html',data)



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def Whishlist(request):
   data={
       'whishlist':Product.objects.filter(wishlist=True)
   }
   return render(request, 'wishlist/index.html',data)

def Card(request):
   
   return render(request, 'card/index.html')