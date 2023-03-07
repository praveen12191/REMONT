from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
def reg(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['password']
        password2 = request.POST['cpassword']
        print(username)
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User name taken')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                
            else:
                user = User.objects.create_user(username=username,email=email,phone=phone,password1=password1,password2=password2)
                user.save();
                messages.info(request,'Account created succesfully')
                return redirect('emp_login')
        else:
            messages.info(request,'Someting went Wrong')
        return redirect('emp_reg')
    else:
        return render(request,'base/emp_reg.html')
def log(request):
    if request.method=='POST':
      username = request.POST['username']
      password = request.POST['password']
      user = auth.authenticate(username=username,password=password)
      if user is not  None :

        auth.login(request, user)
        return redirect('job')
      else:
        messages.info(request,'Invalid username or password')
        return redirect('emp_login')
    else:
        return render(request,'base/emp_log.html')
def logout(request):
   auth.logout(request)
   return redirect('home')
    