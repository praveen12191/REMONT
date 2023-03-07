from email.message import EmailMessage
from tokenize import generate_tokens
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import get_user_model 
from django1 import settings
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_text
from . tokens import generate_token
from django.core.mail import EmailMessage,send_mail

def register(request):
    print(request.method)
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        
        password1 = request.POST['password1']
        password2 = request.POST['password2'] 
      
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User name taken')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                
            else:
                user = User.objects.create_user(username=username,email=email,password=password1)
                
                user.is_active = False
                user.save();
                #welcome email
                message = "hai "+user.username+" Thank you for registering to REMONT..."
                from_email = settings.EMAIL_HOST_USER
                to_list = [user.email]
                send_mail("",message,from_email,to_list,fail_silently=True)

                #email confirm
                messages.info(request,'Account created succesfully we have send you a confirmation Email')
                current_site = get_current_site(request)
                email_sub = "Confirm your email"
                mes = render_to_string('email_confirm.html',{
                    'name' : user.username,
                    'domain':current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':generate_token.make_token(user)
                })
                email1 = EmailMessage(
                    email_sub,
                    mes,
                    settings.EMAIL_HOST_USER,
                    [user.email],
                )
                email1.fail_silently = True
                email1.send()
                return redirect('login')
        else:
            messages.info(request,'Someting went Wrong')
        return redirect('register')
    else:
        
        print("not created")
        return render(request,'base/register.html')


def logout(request):
   auth.logout(request)
   return redirect('home')
def booking(request):
    return render(request,'base/booking.html')
    
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk*uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user = None 
    if user is not None and generate_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request,user)
        return redirect('home')
    else:
        return render(request, 'activation_fails.html')
def login(request):

  print(request.method)
  if request.method=='POST':
      username = request.POST['username']
      password = request.POST['password']
      user = auth.authenticate(username=username,password=password)
      if user is not  None : 

        auth.login(request, user)
        return redirect('home')
      else:
        messages.info(request,'Invalid username or password')
        return redirect('login')
  else:
       return render(request,'base/login.html')