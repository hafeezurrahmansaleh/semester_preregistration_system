from django.shortcuts import render
from adminpanel.models import Courses
from student.models import StudentInfo
from .models import TeacherInfo

def teacherPanelHome(request):
    teacher = TeacherInfo.objects.get(tEmail = request.user.email)
    studentInfo = StudentInfo.objects.filter(stAdvisor=teacher)
    course = Courses.objects.all()
    print(teacher.tName)
    context = {
        'courses' : course,
        'teachers': teacher,
        'students' :studentInfo
    }

    return render(request, 'teacherpanel/tphome.html',context)
