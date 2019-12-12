from django.shortcuts import render,redirect
from teacher.models import TeacherInfo
from student.models import StudentInfo
from .models import *

def login(request):
    return render(request, 'adminpanel/login.html')

def index(request):
    course = Courses.objects.all()
    teacher = TeacherInfo.objects.all()
    student = StudentInfo.objects.all()
    context = {
        'courses':course,
        'teachers':teacher,
        'students':student
    }
    return render(request, 'adminpanel/index.html',context)
def insert(request):
    table = request.POST['editorTitle']
    if table == 'course':
        courseCode = request.POST['ccode']
        courseTitle = request.POST['ctitle']
        courseCredit = request.POST['ccredit']
        courseLevel = request.POST['clevel']
        courseTerm = request.POST['cterm']
        newCourse = Courses(courseCode=courseCode,courseTitle=courseTitle,courseCredit=courseCredit,level=courseLevel,term = courseTerm)
        newCourse.save()
        return redirect('index')

    elif table == 'student':
        studentID = request.POST['stid']
        studentName = request.POST['stname']
        studentEmail = request.POST['stemail']
        studentGender = request.POST['stgender']
        studentPhone = request.POST['stphone']
        studentAdvisor = request.POST['stadvisor']
        newStudent = StudentInfo(stID=studentID,stName=studentName,stEmail=studentEmail,stGender=studentGender,stPhone=studentPhone,stAdivsor=studentAdvisor)
        newStudent.save()
        return redirect('index')

    elif table =='teacher':
        teacherID = request.POST['tid']
        teacherName = request.POST['tname']
        teacherInitial = request.POST['tinitial']
        teacherDesignation = request.POST['tdesingnation']
        teacherPhone = request.POST['tphone']
        teacherEmail = request.POST['temail']
        newTeacher = TeacherInfo(tID=teacherID,tName=teacherName,tInitial=teacherInitial,tDesignation=teacherDesignation,tPhone=teacherPhone,tEmail=teacherEmail)
        newTeacher.save()
        return redirect('index')