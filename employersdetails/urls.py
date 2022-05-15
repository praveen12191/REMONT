from django.contrib import admin
from django.urls import path,include
from.import views
urlpatterns = [
    path('empdetails',views.emp_home,name="empdetails"),
  
]