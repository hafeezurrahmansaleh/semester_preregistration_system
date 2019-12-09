from django.db import models
from student.models import StudentInfo
from teacher.models import TeacherInfo

class AdminInfo(models.Model):
    adminID = models.CharField(max_length=20, unique=True)
    adminName = models.CharField(max_length=20)
    adminEmail = models.CharField(max_length=20)


class Courses(models.Model):
    courseCode = models.CharField(max_length=10, unique=True)
    courseTitle = models.CharField(max_length=50)
    courseCredit = models.IntegerField()
    level = models.IntegerField()
    term = models.IntegerField()

class SemesterInfo(models.Model):
    semesterCode = models.IntegerField(unique=True)
    semester = models.CharField(max_length=10)
    course = models.ForeignKey(Courses,on_delete=models.CASCADE)
    totalSection = models.IntegerField()

class CoursePreRegistration(models.Model):
    student = models.ForeignKey(StudentInfo, on_delete= models.CASCADE)
    course = models.ForeignKey(Courses, on_delete= models.CASCADE)
    semester = models.ForeignKey(SemesterInfo, on_delete=models.CASCADE)
    section = models.CharField(max_length=5)
    paymentStatus = models.CharField(max_length=20)