
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from adminpanel.models import Courses, SemesterInfo,CoursePreRegistration
from student.models import StudentInfo
from .models import TeacherInfo
from django.db.models import Sum
from django.shortcuts import render
from adminpanel.models import Courses
from student.models import StudentInfo
from .models import TeacherInfo
def teacherPanelHome(request):
    teacher = TeacherInfo.objects.get(tEmail = request.user.email)
    studentInfo = StudentInfo.objects.filter(stAdvisor=teacher)
    semester=SemesterInfo.objects.get(semesterCode='201')
    regStudents= CoursePreRegistration.objects.filter(student__stAdvisor=teacher, semester=semester).values('student__stID','student__stName').order_by('student__stID').annotate(credit=Sum('course__courseCredit')).distinct()
    course = Courses.objects.all()
    print(teacher.tName)
    context = {
        'courses' : course,
        'teachers': teacher,
        'students' :studentInfo,
        'regStudents' :regStudents,
    }
    return render(request, 'teacherpanel/tphome.html',context)

def advisestudent(request, stID):
    tEmail = request.user.email
    advisor = TeacherInfo.objects.get(tEmail=tEmail)
    if(StudentInfo.objects.get(stID=stID, stAdvisor=advisor)):
        student = StudentInfo.objects.get(stID=stID)
        courses = Courses.objects.all()
        semester = SemesterInfo.objects.all()
        context = {
            'courses': courses,
            'student': student,
            'semesters': semester
        }
        return render(request, 'studentpanel/stphome.html', context)
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

