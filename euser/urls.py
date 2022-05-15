from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('e_register/',views.register,name='eregister'),
    path('profile/',views.profile,name='profile'),
    
]