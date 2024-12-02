from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='root'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('contact/', views.contact, name='contact'),
    path('products/', views.products, name='products'),
    path('product/<int:pk>', views.product, name='product'),
    path('sales/', views.sales, name='sales'),
]