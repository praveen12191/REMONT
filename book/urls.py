from django.contrib import admin
from django.urls import path,include
from.import views
urlpatterns = [
    path('booking',views.book,name="booking"),
  
]