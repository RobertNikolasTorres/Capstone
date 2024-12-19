from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms 
from django.db.models import Q

# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def about(request):
    return render(request, 'about.html')

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        searched = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
        if not searched:
            messages.success(request, "That Product Doesn't Exist...")
            return render(request, "search.html", {})
        else:
            return render(request, "search.html", {'searched':searched})
    else:
        return render(request, "search.html", {})

def product (request,pk):
     product = Product.objects.get(id=pk)
     return render(request, 'product.html',{'product':product})

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def sales(request):
    products = Product.objects.all()
    return render(request, 'sales.html', {'products': products})

def category(request, foo):
    #foo = foo.replace('-', ' ')
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products':products, 'category':category})  
    except:
        messages.success(request, ("That Category Doesn't Exist..."))
        return redirect('products')

def category_summary(request):
     categories = Category.objects.all()
     return render(request, 'category_summary.html', {'categories':categories})

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
            return render(request, 'login.html')

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
            return render(request, 'register.html', {'form': form })

     


    