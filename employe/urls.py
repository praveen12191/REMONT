from user.views import register
from django.urls import path,include
from django.contrib.auth import views as auth_views
from.import views
from user import views as user_views
from .views import postlistvies,detailvies

urlpatterns = [
    # inserd of views.home need to add
    path('e_home',postlistvies.as_view(),name='ehome'),

    #path('post/<int:pk>/',detailvies.as_view(),name='post_detail'),
    path('register/',user_views.register,name='eregister'),
    #path('profile/',user_views.profile,name='profile'),
    path('e_login/',auth_views.LoginView.as_view(template_name='base/new/elogin.html'),name='elogin'),
    path('logout/',auth_views.LogoutView.as_view(template_name='base/new/logout.html'),name='logout'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='base/new/password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='base/new/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='base/new/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='base/new/password_reset_complete.html'),name='password_reset_complete'),
    path('about/',views.about,name='about')
]

