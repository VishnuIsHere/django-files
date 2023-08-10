from django.shortcuts import render
from django.http import HttpResponse
from . models import *


# Create your views here.
def home(request):
    c={
        'c_dis': course.objects.all()
    }
    return render(request,'home.html',c)

def about(request):
    return render(request,'about.html')

def product(request):
    d = {
        'display': student.objects.all()
       
    }
    return render(request,'p.html',d) 
