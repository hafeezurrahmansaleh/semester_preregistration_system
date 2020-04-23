from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def advisorHome(request):
    id = 1
    advisor= Advisor.objects.get(pk=id)
    course= Course.objects.filter(courseTeacher=advisor)
    context = {
        'adv': advisor,
        'crs': course,
    }
    return render(request,'advisorpanel/advisorHome.html',context)