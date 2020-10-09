from django.db import models
from student.models import StudentInfo
from teacher.models import TeacherInfo
from users.models import User


class AdminInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Courses(models.Model):
    courseCode = models.CharField(max_length=20, unique=True)
    courseTitle = models.CharField(max_length=100)
    courseCredit = models.IntegerField()
    level = models.IntegerField()
    term = models.IntegerField()
    totalSection = models.IntegerField(null=True)

class SemesterInfo(models.Model):
    semesterCode = models.IntegerField(unique=False)
    semesterTitle = models.CharField(max_length=20)
    regOpenDate = models.DateField()
    regCloseDate = models.DateField()

class CourseSection(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    semester = models.ForeignKey(SemesterInfo, on_delete=models.CASCADE)
    totalSection = models.IntegerField()

class CoursePreRegistration(models.Model):
    student = models.ForeignKey(StudentInfo, on_delete= models.CASCADE, related_name="studentCredits")
    course = models.ForeignKey(Courses, on_delete= models.CASCADE, related_name="registered")
    semester = models.ForeignKey(SemesterInfo, on_delete=models.CASCADE)
    section = models.CharField(max_length=5)
    paymentStatus = models.CharField(max_length=20)
    

class Remarks(models.Model):
    student =models.ForeignKey(StudentInfo, on_delete= models.CASCADE)
    semester = models.ForeignKey(SemesterInfo, on_delete=models.CASCADE)
    remark = models.CharField(max_length=500, null=True)
    

class CourseRegistration(models.Model):
    student =models.ForeignKey(StudentInfo, on_delete= models.CASCADE)
    semester = models.ForeignKey(SemesterInfo, on_delete=models.CASCADE)
    registered = models.BooleanField(default=False)
    
    
class WaiverInfo(models.Model):
    studentID =models.CharField(max_length=40)
    semester = models.ForeignKey(SemesterInfo, on_delete=models.CASCADE)
    existingWaiver = models.IntegerField()
    specialWaiver = models.IntegerField()
    totalWaiver = models.IntegerField()
    amountofWaiver = models.IntegerField()
    percentofWaiver = models.IntegerField()
    
class PaymentInfo(models.Model):
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    semester = models.ForeignKey(SemesterInfo, on_delete=models.CASCADE)
    paymentStatus = models.BooleanField(default=False)
    comment = models.CharField(null=True, max_length=500)



