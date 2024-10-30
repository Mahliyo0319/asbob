from django.contrib import admin
from django.urls import path
from backend.views import *
admin.site.login_template='backend_admin/login/index.html'
from django.urls import path
from . import views

urlpatterns = [
    path('' , Home ,name='home'),
    path('register/' , Register),
    path('login/', Login),
    path('logout/', Logout),
    path('product_details/<int:id>', Product_details),
    path('wishlist/', Whishlist),
    path('card/', Card),
]



