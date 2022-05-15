from django.shortcuts import render
from .models import product
def home(request):
    all = product.objects.all()
   
    return render(request,"base/index.html",{'all':all})



