from django.shortcuts import render
def reg(request):
    return render(request,'base/emp_reg.html')
def log(request):
    return render(request,'base/emp_log.html')