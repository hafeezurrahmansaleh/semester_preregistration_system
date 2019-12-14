import jsonify as jsonify
from django.core import serializers
# from django.core.serializers import json
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt
from users.models import User
import json

from .models import *
from adminpanel.models import Courses, SemesterInfo, CoursePreRegistration

def studentPanelHome(request):
    courses = Courses.objects.all()
    student = StudentInfo.objects.get(stEmail = request.user.email)
    semester = SemesterInfo.objects.all()
    context = {
        'courses': courses,
        'student':student,
        'semesters' : semester
    }
    return render(request, 'studentpanel/stphome.html',context)
@csrf_exempt
def findCourse(request):
    cid = request.POST['cid']
    courses = Courses.objects.filter(pk=cid)
    # print(level+semester)
    data = serializers.serialize('json', courses)
    return HttpResponse(data)
@csrf_exempt
def registerCourse(request):
    courseCode = request.POST['ccode']
    section = request.POST['section']
    semestercode = request.POST['semester']
    print(courseCode)
    # try:
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
@csrf_exempt
def dropCourses(request):
    courseCode = request.POST['ccode']
    semester = request.POST['semester']
    student = StudentInfo.objects.get(stEmail = request.user.email)
    course = Courses.objects.get(courseCode=courseCode)
    registeredCourse=CoursePreRegistration.objects.get(student=student,course=course,semester=semester)
    registeredCourse.delete()
    return HttpResponse('success')
@csrf_exempt
def findRegisteredCourses(request):
    student = StudentInfo.objects.get(stEmail=request.user.email)
    semesterCode = request.POST['semester']
    semester = SemesterInfo.objects.get(semesterCode = semesterCode)
    courses = CoursePreRegistration.objects.filter(semester=semester, student=student).values('course__courseCode', 'course__courseTitle','course__courseCredit', 'course_id', 'section','semester__semesterTitle')
    # print(level+semester)
    data = json.dumps(list(courses))
    # data = serializers.serialize('json', courses)
    return HttpResponse(data)