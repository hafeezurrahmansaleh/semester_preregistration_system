from django.shortcuts import render
<<<<<<< HEAD
from adminpanel.models import Courses
from student.models import StudentInfo
from .models import *

def teacherPanelHome(request):

    teacher = TeacherInfo.objects.get(tEmail = request.user.email)
    studentInfo = StudentInfo.objects.filter(stAdvisor=teacher)
    course = Courses.objects.all()
    print(teacher.tName)
    context = {
        'courses' : course,
        'teachers': teacher,
        'students' :studentInfo
=======
<<<<<<< HEAD
from adminpanel.models import Courses
=======
from django.contrib.auth.decorators import login_required
from users.decorators import teacher_required
>>>>>>> 832dd4ff9d6c127e8db85eb2ac401c9342f95669
from .models import *

def teacherPanelHome(request):
    id = 1
    teacher = TeacherInfo.objects.get(pk=id)
    course = Courses.objects.all()
    context = {
        'teacher' : teacher,
        'course' : course
>>>>>>> refs/remotes/origin/master
    }
    return render(request, 'teacherpanel/tphome.html',context)