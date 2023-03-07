from django.contrib import admin
from django.urls import path,include
from . import views
from django_email_verification import urls as mail_urls

urlpatterns = [
    path('register',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('booking',views.booking,name='booking'),
    path('email/',include(mail_urls)),
    path('activate/<uidb64>/<token>',views.activate,name='activate'),
]