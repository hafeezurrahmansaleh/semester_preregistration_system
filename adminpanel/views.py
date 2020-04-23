import openpyxl
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt

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
        'semesters':semester,
    }
    return render(request, 'adminpanel/index.html',context)
def insert(request):
    try:
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
            print(studentAdvisor)
            advisor = TeacherInfo.objects.get(tInitial=studentAdvisor)

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
            # formatedregOpenDate = regOpenDate.strftime("%YYYY-%MM-%DD")
            regClosedDate = request.POST['regClosedDate']
            # formatedregClosedDate = regClosedDate.strftime("%YYYY-%MM-%DD")
            print(regOpenDate)

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
    except :
        return redirect('error404','Something wromh!!!')




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

def studentList(request, courseCode, semesterID):

    # student = StudentInfo.objects.get(stEmail=request.user.email)
    # semesterCode = request.POST['semester']
    # courseCode = request.POST['ccode']
    semester = SemesterInfo.objects.get(semesterCode=semesterID)
    course = Courses.objects.get(id=courseCode)
    studentlistA = CoursePreRegistration.objects.filter(course=course,semester=semester,section='A')
    studentlistB = CoursePreRegistration.objects.filter(course=course,semester=semester,section='B')
    studentlistC = CoursePreRegistration.objects.filter(course=course,semester=semester,section='C')
    studentlistD = CoursePreRegistration.objects.filter(course=course,semester=semester,section='D')
    studentlistE = CoursePreRegistration.objects.filter(course=course,semester=semester,section='E')
    studentlistF = CoursePreRegistration.objects.filter(course=course,semester=semester,section='F')
    context = {
        'course':course,
        'studentlistsA': studentlistA,
        'studentlistsB': studentlistB,
        'studentlistsC': studentlistC,
        'studentlistsD': studentlistD,
        'studentlistsE': studentlistE,
        'studentlistsF': studentlistF,
    }
    return render(request, 'adminpanel/studentlist.html',context)


# def fupload(request):
#
#     if "GET" == request.method:
#         return render(request, 'adminpanel/index.html', {})
#     else:
#         doc = request.FILES
#         excel_file = doc['excel_file']
#         if (str(excel_file).split(‘.’)[-1] == “xls”):
#             data = xls_get(excel_file, column_limit=4)
#         elif (str(excel_file).split(‘.’)[-1] == “xlsx”):
#             data = xlsx_get(excel_file, column_limit=4)
#         else:
#             return redirect( < your_upload_file_fail_url >)
@csrf_exempt
def fileUpload(request):
    if "GET" == request.method:
        return render(request, 'adminpanel/index.html', {})
    else:
        doc = request.FILES
        excel_file = doc['excel_file']

        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)

        # getting all sheets
        sheets = wb.sheetnames
        print(sheets)

        # getting a particular sheet
        worksheet = wb["Sheet1"]
        print(worksheet)

        # getting active sheet
        active_sheet = wb.active
        print(active_sheet)

        # reading a cell
        # print(worksheet["B"][0].value)

        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        counter = 0
        table = request.POST['fileuploader']
        if table == 'teacher':
         for row in worksheet.iter_rows():
            row_data = list()
            # print(row[0].value)

            for cell in row:
                row_data.append(str(cell.value))
                if (counter == 0):
                   continue
                t = TeacherInfo.objects.filter(tID=(row[3].value))
                if (t.count() == 0):
                    try:
                        TeacherInfo.objects.create(
                            tName=row[0].value,
                            tInitial=row[1].value,
                            tDesignation=row[2].value,
                            tID=row[3].value,
                            tPhone=row[4].value,
                            tEmail=row[5].value
                        )
                    except:
                        advisor = ""
            excel_data.append(row_data)
            print(row_data)
            counter+=1
        elif table == 'student':
            for row in worksheet.iter_rows():
                row_data = list()
                # print(row[0].value)

                for cell in row:
                    row_data.append(str(cell.value))
                    if (counter == 0):
                        continue
                    s = StudentInfo.objects.filter(stID=(row[0].value))
                    if (s.count() == 0):
                        try:
                            advisor = TeacherInfo.objects.get(tInitial=row[5].value)
                        except:
                            advisor = ""
                        StudentInfo.objects.create(
                            stID=row[0].value,
                            stName=row[1].value,
                            stGender=row[2].value,
                            stPhone=row[3].value,
                            stEmail=row[4].value,
                            stAdvisor=advisor,
                        )

                excel_data.append(row_data)
                print(row_data)
                counter += 1
        elif table == 'course':
            for row in worksheet.iter_rows():
                row_data = list()
                # print(row[0].value)

                for cell in row:
                    row_data.append(str(cell.value))
                    if (counter == 0):
                        continue
                    c = Courses.objects.filter(courseCode=(row[0].value))
                    if (c.count() == 0):
                        try:
                            Courses.objects.create(
                                courseCode=row[0].value,
                                courseTitle=row[1].value,
                                courseCredit=row[2].value,
                                level=row[3].value,
                                term=row[4].value
                            )
                        except:
                            advisor = ""

                excel_data.append(row_data)
                print(row_data)
                counter += 1
        return redirect(index)

    
def error404(request, msg):
    return render(request,'404.html', {'message':msg})

def prevPage(request):
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))