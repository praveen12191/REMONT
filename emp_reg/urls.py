from django.contrib import admin 
from django.urls import path,include
from . import views
urlpatterns = [
    path('emp_reg',views.reg,name="emp_reg"),
    path('emp_login',views.log,name="emp_login")
]

