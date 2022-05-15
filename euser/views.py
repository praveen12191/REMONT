from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from  .form import profile_update, user_uptade, useregister
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method=='POST':
        # insterd of using Usercreationform we can use useregister because we created additional fields in form.py 
        #form = UserCreationForm(request.POST)
        form = useregister(request.POST)
        if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request,f'Account created for {username} now you can login')
                return redirect('elogin')
    else:
            form = useregister()
    return render(request,'base/new/eregister.html',{'form':form})
@ login_required
def profile(request):
        if request.method=='POST':
                u_form = user_uptade(request.POST,instance=request.user)
                p_form = profile_update(request.POST,request.FILES,instance=request.user.profile)
                if u_form.is_valid() and p_form.is_valid():
                        u_form.save()
                        p_form.save()
                        messages.success(request, f'Your account changed')
                        return redirect('profile')
        else:
                u_form = user_uptade(instance=request.user)
                p_form = profile_update(instance=request.user.profile)
                # need to send two form so going with context
        context = {
                'u_form' : u_form,
                'p_form' : p_form
        }
        

        return render(request,'base/new/profile.html',context)
