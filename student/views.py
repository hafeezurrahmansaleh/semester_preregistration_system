import jsonify as jsonify
from django.core import serializers
# from django.core.serializers import json
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse,redirect
from django.shortcuts import render, HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt
from users.models import User
import json
from django.contrib.auth.decorators import login_required
from users.decorators import student_required
from .models import *
from adminpanel.models import Courses, SemesterInfo, CoursePreRegistration,WaiverInfo,\
	PaymentInfo, CourseRegistration
#email
from django.core.mail import send_mail
from django.conf import settings


@login_required
@student_required
def studentPanelHome(request):
    courses = Courses.objects.all().order_by('level', 'term', 'courseCode')
    try:
        student = StudentInfo.objects.get(stID = request.user.username)
    except:
        student = 'not found'
    try:
        regstatus = CourseRegistration.objects.get(student_id=student.id)
    except:
        regstatus = 'not found'
    semester = SemesterInfo.objects.all()
    currentsemester = SemesterInfo.objects.get(semesterCode='201')
    try:
        waiver = WaiverInfo.objects.get(studentID=student.stID)
    except:
        print("Waiver nai")
        waiver = ''
    try:
        payment = PaymentInfo.objects.get(student=student, semester=currentsemester )
    except:
        print("Payment nai")
        payment = ''
    context = {
        'courses': courses,
        'student':student,
        'semesters' : semester,
        'waiver' : waiver,
        'payment':payment,
        'regstatus':regstatus,
    }
    return render(request, 'studentpanel/stphome.html',context)


@login_required
@student_required
@csrf_exempt
def findCourse(request):
    cid = request.POST['cid']
    courses = Courses.objects.filter(pk=cid)
    # print(level+semester)
    data = serializers.serialize('json', courses)
    return HttpResponse(data)


@login_required
@student_required
@csrf_exempt
def registerCourse(request):
    courseCode = request.POST['ccode']
    section = request.POST['section']
    semestercode = request.POST['semester']

    # try:
    print(section)
    student = StudentInfo.objects.get(stEmail = request.user.email)
    course = Courses.objects.get(courseCode=courseCode)
    semester = SemesterInfo.objects.get(semesterCode=semestercode)

    registration = CoursePreRegistration(student = student, course = course, semester=semester,section=section,paymentStatus='0')
    registration.save()
    msg="successfully saved"
    # except Exception as e:
    # msg=e.__cause__
    return HttpResponse(msg)

# @csrf_exempt
# def updateregistercourse(request):
#     courseCode = request.POST['ccode']
#     section = request.POST['section']
#     semester = request.POST['semester']
#     try:
#         student = StudentInfo.objects.get(pk=sid)
#         course = Courses.objects.get(courseCode=courseCode)
#         registration = CoursePreRegistration.objects.get(student=student,course=course,semester=semester
#             student = student, course = course, semester=semester,section=section,paymentStatus='0')
#         registration.save()
#         msg="successfully saved"
#     except Exception as e:
#         msg=e.__cause__
#     return HttpResponse(msg)


@login_required
@student_required
@csrf_exempt
def dropCourses(request):

    # courseCode = request.POST['ccode']
    semesterCode = request.POST['semester']
    student = StudentInfo.objects.get(stEmail = request.user.email)
    # course = Courses.objects.get(courseCode=courseCode)
    semester = SemesterInfo.objects.get(semesterCode=semesterCode)
    CoursePreRegistration.objects.filter(student=student,semester=semester).delete()
    return HttpResponse('success')


@login_required
@student_required
@csrf_exempt
def findRegisteredCourses(request):
    student = StudentInfo.objects.get(stEmail=request.user.email)
    semesterCode = request.POST['semester']
    semester = SemesterInfo.objects.get(semesterCode = semesterCode)
    courses = CoursePreRegistration.objects.filter(semester=semester, student=student).values('course__courseCode', 'course__courseTitle','course__courseCredit', 'course_id', 'section','semester__semesterTitle', 'course__totalSection')
    # print(level+semester)
    data = json.dumps(list(courses))
    # data = serializers.serialize('json', courses)
    print(data)
    return HttpResponse(data)

@login_required
@student_required
@csrf_exempt
def getstudentpersection(request):
    sec = request.POST['section']
    ccode = request.POST['ccode']
    semcode= request.POST['semester']
    semester = SemesterInfo.objects.get(semesterCode=semcode)
    course=Courses.objects.get(courseCode=ccode)
    count = CoursePreRegistration.objects.filter(semester=semester, course__courseCode=ccode,section=sec).values('id').count()
    print(sec,ccode,semcode)
    data={
        'countvalue':count,
        'sec':sec,
    }
    return JsonResponse(data)
    

@csrf_exempt
def addpaymentstatus(request):
    student = StudentInfo.objects.get(stID=request.user.username)
    semcode = request.POST['semester']
    semester = SemesterInfo.objects.get(semesterCode=semcode)
    comment = request.POST['studentComment']
    paymentStatus = request.POST['paymentStatus']
    advisor = TeacherInfo.objects.get(pk = student.stAdvisor_id)
    if(paymentStatus):
        pstat = "Paid"
    else:
        pstat = "Not paid"

    if(PaymentInfo.objects.filter(student=student, semester = semester).exists()):
        status = PaymentInfo.objects.get(student=student, semester=semester)
        status.comment = comment
        status.paymentStatus = paymentStatus
        status.save()
        msg = "Successfully Updated!"
    else:
        status = PaymentInfo(student=student, semester=semester, comment=comment, paymentStatus=paymentStatus)
        status.save()
        msg = "Successfully Saved!"
    try:
        subject = 'Payment Status of Summer 2020'
        message = "My Student ID is: " + student.stID + '\nMy Payment Status is: '+ pstat + '\nDetails: '+comment
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [advisor.tEmail, ]
        send_mail(subject, message, email_from, recipient_list)
        msg='Successfully saved and this information has been send to your advisor'
    except:
        msg = 'Saved but failed to send to your advisor'
    return HttpResponse(msg)
@login_required
def gototohomepage(request):
    if(request.user.is_admin):
        print('Admin')
        return redirect('/adminpanel/index')
    elif(request.user.is_teacher):
        print('Teacher')
        return redirect('/teacher/')
    elif (request.user.is_student):
        print('Student')
        return redirect('/student/')