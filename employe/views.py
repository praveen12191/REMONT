from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView,DetailView
"""post = [ 
    {
        'title':'There no Title',
        'from':'From tiruppur',
        'name':'Praveen',
        'date':'11-7-2021',

        'content':'From CSE dep of sri eshwar college'
    },
    {
        'title':'There is nothing',
        'from':'From CBE',
        'name':'Saravanan',
        'date':'10-7-2021',
        'content':'From CSE dep of sri eshwar college'
    }
]"""


def ehome (request):
    context ={
        'post':Post.objects.all()
    }
    return render(request,'base/new/web.html',context)
# convering all post into list format
class postlistvies(ListView):
    model = Post
    template_name = 'base/new/web.html'
    context_object_name= 'post'
    #ordering = ['-date_posted']
class detailvies(ListView):# if we touch the induadual post show the details
    model = Post # htmp in the format <app>/<modes>_<viewtype>.html
    

def about(request):
    return render(request,'base/new/about.html',{'title':'Boom'})