from django.shortcuts import render
from .models import jobs

def job(request):
    ob1 = jobs()
    ob1.job_name = "hello"
    ob1.job_dec = "how are you"
    ob1.expo = 4 
    ob1.img = "line-dec.png"
    ob2 = jobs()
    ob2.job_name = "hello"
    ob2.job_dec = "how are you"
    ob2.expo = 4 
    ob2.img = "line-dec.png"
    ob = [ob1,ob2]

    return render(request,'base/jobs.html',{'ob':ob})
