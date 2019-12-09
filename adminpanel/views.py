from django.shortcuts import render

from .models import *

def login(request):
    return render(request, 'adminpanel/login.html')

def index(request):
    courses = Courses.objects.all()
    context = {
        'courses':courses
    }
    return render(request, 'adminpanel/index.html',context)