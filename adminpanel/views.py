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
    semester = SemesterInfo.objects.all()
    context = {
        'courses':course,
        'teachers':teacher,
        'students':student,
        'semesters':semester
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
        if Courses.objects.filter(courseCode=courseCode):
            course = Courses.objects.get(courseCode=courseCode)
            course.courseTitle = courseTitle
            course.courseCredit = courseCredit
            course.level = courseLevel
            course.term = courseTerm
            course.save()
        else:
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
        advisor = TeacherInfo.objects.get(tName=studentAdvisor)
        if StudentInfo.objects.filter(stID=studentID).exists():
            student = StudentInfo.objects.get(stID=studentID)
            student.stName = studentName
            student.stEmail = studentEmail
            student.stGender = studentGender
            student.stPhone = studentPhone
            student.stAdvisor = advisor
            student.save()
        else:
            newStudent = StudentInfo(stID=studentID,stName=studentName,stEmail=studentEmail,stGender=studentGender,stPhone=studentPhone,stAdvisor=advisor)
            newStudent.save()

        return redirect('index')

    elif table =='teacher':
        print(table)
        teacherID = request.POST['tid']
        teacherName = request.POST['tname']
        teacherInitial = request.POST['tinitial']
        teacherDesignation = request.POST['tdesingnation']
        teacherPhone = request.POST['tphone']
        teacherEmail = request.POST['temail']
        if TeacherInfo.objects.filter(tID= teacherID).exists():
            teacher = TeacherInfo.objects.get(tID=teacherID)
            teacher.tName = teacherName
            teacher.tInitial = teacherInitial
            teacher.tDesignation = teacherDesignation
            teacher.tPhone = teacherPhone
            teacher.tEmail = teacherEmail
            teacher.save()
        else:
            newTeacher = TeacherInfo(tID=teacherID,tName=teacherName,tInitial=teacherInitial,tDesignation=teacherDesignation,tPhone=teacherPhone,tEmail=teacherEmail)
            newTeacher.save()

        return redirect('index')
    elif table =='semester':
        semesterCode = request.POST['scode']
        semesterTitle = request.POST['stitle']
        regOpenDate = request.POST['regOpenDate']
        regClosedDate = request.POST['regClosedDate']
        if SemesterInfo.objects.filter(semesterCode=semesterCode).exists():
            semester = SemesterInfo.objects.get(semesterCode=semesterCode)
            semester.semesterCode = semesterCode
            semester.semesterTitle = semesterTitle
            semester.regOpenDate = regOpenDate
            semester.regClosedDate = regClosedDate
            semester.save()
        else:
            newSemester = SemesterInfo(semesterCode=semesterCode,semesterTitle=semesterTitle,regOpenDate=regOpenDate,regCloseDate=regClosedDate)
            newSemester.save()

        return redirect('index')




def teacherDelete(request,tid):
    teacher = TeacherInfo.objects.get(pk=tid)
    teacher.delete()
    return redirect('index')

def studentDelete(request,stid):
    student = StudentInfo.objects.get(pk=stid)
    student.delete()
    return redirect('index')

def courseDelete(request,courseCode):
    course = Courses.objects.get(pk=courseCode)
    course.delete()
    return redirect('index')

def studentList(request):
    studentlist = CoursePreRegistration.objects.all()
    context = {
        'studentlists': studentlist,
    }
    return render(request, 'adminpanel/studentlist.html',context)
