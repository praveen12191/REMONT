from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

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
                user.save();
                messages.info(request,'Account created succesfully')
                return redirect('login')
        else:
            messages.info(request,'Someting went Wrong')
        return redirect('register')
    else:
        
        print("not created")
        return render(request,'base/register.html')

 
  

def login(request):

  print(request.method)
  if request.method=='POST':
      username = request.POST['username']
      password = request.POST['password']
      user = auth.authenticate(username=username,password=password)
      if user is not  None : #

        auth.login(request, user)
        return redirect('home')
      else:
        messages.info(request,'Invalid username or password')
        return redirect('login')
  else:
       return render(request,'base/login.html')
def logout(request):
   auth.logout(request)
   return redirect('home')
def booking(request):
    return render(request,'base/booking.html')
    
 