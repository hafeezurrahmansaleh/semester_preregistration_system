
from django.core.serializers import json
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required
from users.decorators import teacher_required
from adminpanel.models import Courses, SemesterInfo,CoursePreRegistration,CourseRegistration, PaymentInfo
from student.models import StudentInfo
from .models import TeacherInfo
from django.db.models import Sum, Count
from django.shortcuts import render
from adminpanel.models import Courses,Remarks
from student.models import StudentInfo
from .models import TeacherInfo
#email
from django.core.mail import send_mail
from django.conf import settings

def teacherPanelHome(request):
    teacher = TeacherInfo.objects.get(tEmail = request.user.email)
    studentInfo = StudentInfo.objects.filter(stAdvisor=teacher)
    semester=SemesterInfo.objects.get(semesterCode='201')
    regStudents= CoursePreRegistration.objects.filter(student__stAdvisor=teacher, semester=semester).values('student_id', 'student__stID','student__stName', 'student__remarks__remark').annotate(credit=Sum('course__courseCredit')).distinct()
    # notregistered = StudentInfo.objects.exclude(stID=regStudents.studen__stID)
    notregistered = studentInfo.exclude(stID__in=[o['student__stID'] for o in regStudents]).values('id','stID','stName','stPhone','remarks__remark')
    course = Courses.objects.all().order_by('level', 'term', 'courseCode')
    regstatus = CourseRegistration.objects.filter(semester__semesterCode='201',
                                               student__stAdvisor_id=teacher.id).values('student__stID','registered')
    print(teacher.tName)
    context = {
        'courses' : course,
        'teachers': teacher,
        'students' :studentInfo,
        'regStudents' :regStudents,
        'notregistered' :notregistered,
        'regstatus': regstatus,
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
        
        
@csrf_exempt
def registeredCourses(request):
    # student = StudentInfo.objects.get(stEmail=request.user.email)
    semesterCode = request.POST['semester']
    stID=request.POST['stID']
    student = StudentInfo.objects.get(stID=stID)
    semester = SemesterInfo.objects.get(semesterCode = semesterCode)
    # courses = CoursePreRegistration.objects.filter(semester=semester, student=student).values('course__courseCode', 'course__courseTitle','course__courseCredit', 'course_id', 'section','semester__semesterTitle')
    courses=CoursePreRegistration.objects.filter(semester=semester, student=student).values('course__courseCode', 'course__courseTitle','course__courseCredit', 'course_id', 'section','semester__semesterTitle','student__stName','student_id','student__stID')
    data = json.dumps(list(courses))
    print(data)
    return HttpResponse(data)
    
@csrf_exempt
def saveRemark(request):
    semesterCode = request.POST['semester']
    sid = request.POST['sid']
    remark = request.POST['remark']
    student = StudentInfo.objects.get(pk=sid)
    semester = SemesterInfo.objects.get(semesterCode=semesterCode)
    msg = ""
    if(Remarks.objects.filter(student=student,semester=semester).exists()):
        newRemark = Remarks.objects.get(student=student,semester=semester)
        newRemark.remark = remark
        newRemark.save()
        msg = "Successfully Updated"
    else:
        newRemark = Remarks(student=student, semester=semester, remark=remark)
        newRemark.save()
        msg = "Successfully Added"
    return HttpResponse(msg)
    
@login_required
def updateRegistration(request, sid,sem):
    student = StudentInfo.objects.get(id=sid)
    semester = SemesterInfo.objects.get(semesterCode = sem)
    # courses = CoursePreRegistration.objects.filter(semester=semester, student=student).values('course__courseCode', 'course__courseTitle','course__courseCredit', 'course_id', 'section','semester__semesterTitle')
    regcourses=CoursePreRegistration.objects.filter(semester=semester, student=student).values('id', 'course__courseCode', 'course__courseTitle','course__courseCredit', 'course_id', 'section','semester__semesterTitle','student__stName','student__stID')
    course = Courses.objects.all()
    context={
        'courses':course,
        'regcourses':regcourses,
        'student':student
    }
    return render(request,'teacherpanel/updateregistration.html',context)
@csrf_exempt
def saveCourse(request):
    semid = request.POST['semester']
    sid = request.POST['sid']
    sec = request.POST['section']
    cid = request.POST['cid']
    rid = request.POST['rid']

    if(CoursePreRegistration.objects.filter(course_id=cid,student_id=sid, semester_id=semid).exists()):
        update = CoursePreRegistration.objects.get(pk=rid)
        update.section = sec
        update.save()
        msg = "Successfully Updated!"
    else:
        add = CoursePreRegistration(student_id=sid, semester_id=semid,course_id=cid,section=sec)
        add.save()
        msg = "Successfully Added!"
    return HttpResponse(msg)


@csrf_exempt
def findCourse(request):
    cid = request.POST['cid']
    courses = Courses.objects.filter(pk=cid).values('id','courseCode','courseTitle','courseCredit')
    # print(level+semester)
    data = json.dumps(list(courses))
    # data = serializers.serialize('json', courses)
    print(data)
    return HttpResponse(data)


@csrf_exempt
def dropCourse(request):
    semesterid = request.POST['semester']
    rid = request.POST['rid']
    CoursePreRegistration.objects.get(id=rid).delete()
    print('deleted'+rid)
    return HttpResponse('success')

@login_required
def finalregistration(request, semid, tinitial):
    sdetails = CoursePreRegistration.objects.filter(semester__semesterCode=semid, student__stAdvisor_id=tinitial).values('student__stID','student_id','student__stName','student__stEmail', 'student__stPhone', 'student__remarks__remark').annotate(credit=Count('course__courseCredit')).distinct()
    cdetails = CoursePreRegistration.objects.filter(semester__semesterCode=semid, student__stAdvisor_id=tinitial).values('student__stID','course__courseCode', 'course__courseTitle','course__courseCredit', 'section').distinct()
    status = CourseRegistration.objects.filter(semester__semesterCode=semid, student__stAdvisor_id=tinitial).values('student__stID','registered')
    payments = PaymentInfo.objects.filter(semester__semesterCode='201', student__stAdvisor_id=tinitial)
    global tidforpayment
    tidforpayment = tinitial
    context = {
        'cdetails': cdetails,
        'sdetails': sdetails,
        'status': status,
        'payments':payments,
    }
    return  render(request, 'teacherpanel/finalregistration.html', context)
    
@csrf_exempt
def findregstatus(request):
    semester = request.POST['semester']
    regstatus = CourseRegistration.objects.filter(semester__semesterCode=semester).values('student__stID','student_id', 'registered')
    data = json.dumps(list(regstatus))
    return HttpResponse(data)
@csrf_exempt
def changeregstatus(request):
    sid = request.POST['sid']
    semid = request.POST['semester']
    status = request.POST['status']
    student = StudentInfo.objects.get(stID=sid)
    semester = SemesterInfo.objects.get(semesterCode=semid)
    if( status=='true'):
        stat = False
    else:
        stat = True
    if (CourseRegistration.objects.filter(student__stID=sid, semester__semesterCode=semid).exists()):
        courseregistration = CourseRegistration.objects.get(student__stID=sid, semester__semesterCode=semid)
        courseregistration.registered = stat
        courseregistration.save()
    else:
        courseregistration = CourseRegistration(student=student, semester= semester, registered=stat)
        courseregistration.save()

        try:
	        subject = 'Registration Status of Summer 2020'
	        message = 'Your registration is done for '+semester.semesterTitle+" semester! Please " \
	                                                                          "check " \
	                                                                  "your student portal. " \
	                                                                  "\n\n--------------------- " \
	                                                                  "\nDepartment " \
	                                                                  "of " \
	                                                                  "Software Engineering\n " \
	                                                                  "Daffodil International " \
	                                                                  "University"
	        email_from = settings.EMAIL_HOST_USER
	        recipient_list = [student.stEmail, ]
	        send_mail(subject, message, email_from, recipient_list)
	        msg = 'Successfully saved and this information has been send to your advisor'
        except:
	        msg = 'Saved but failed to send to your advisor'
    return HttpResponse('Done')
    
@csrf_exempt
def findpaymentstatus(request):
    semester = request.POST['semester']
    payments = PaymentInfo.objects.filter(semester__semesterCode=semester,
                                          student__stAdvisor_id=tidforpayment).values(
        'student_id', 'paymentStatus', 'comment')
    data = json.dumps(list(payments))
    return HttpResponse(data)

