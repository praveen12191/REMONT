
from django.shortcuts import render
from .forms import booking,UserCreationForm

def book(request):
    form = booking(request.POST) 
    if form.is_valid: 
        pass 
    else:
        form = booking()
    context ={
        "form":form
    }
    return render(request,"base/book.html", context)
