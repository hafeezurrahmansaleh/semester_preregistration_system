from django.shortcuts import render
from adminpanel.models import Courses
from .models import *

def teacherPanelHome(request):
    id = 1
    teacher = TeacherInfo.objects.get(pk=id)
    course = Courses.objects.all()
    context = {
        'teacher' : teacher,
        'course' : course
    }
    return render(request, 'teacherpanel/tphome.html',context)