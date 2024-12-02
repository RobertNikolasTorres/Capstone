from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms 

# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def product (request,pk):
     product = Product.objects.get(id=pk)
     return render(request, 'pages/product.html',{'product':product})

def products(request):
    products = Product.objects.all()
    return render(request, 'pages/products.html', {'products': products})

def sales(request):
    products = Product.objects.all()
    return render(request, 'pages/sales.html', {'products': products})

def login_user(request):
        if request.method =="POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, ("You have been logged in!"))
                return redirect('home')
            else:
                messages.success(request, ("There was an error"))
                return redirect('login')
        
        else:
            return render(request, 'pages/login.html')

def logout_user(request):
        logout(request)
        messages.success(request, ("You have been logged out..."))
        return redirect('home')

def register_user(request):
        form = SignUpForm()
        if request.method == "POST":
             form = SignUpForm(request.POST)
             if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']

                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request, ("You have registered successfully!"))
                return redirect('home')
             else:
                messages.success(request, ("whoops! There was a problem registering, please try again."))
                return redirect('register')
        else:   
            return render(request, 'pages/register.html', {'form': form })

     


    