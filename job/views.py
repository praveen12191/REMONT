from django.shortcuts import render
from .models import jobs

def job(request):
    ob = jobs.objects.all()

    return render(request,'base/empo.html',{'ob':ob})
