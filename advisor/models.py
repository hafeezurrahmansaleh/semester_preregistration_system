from django.db import models

# Create your models here.
class Advisor(models.Model):
    advisorName = models.CharField(max_length=20)
    advisorID = models.CharField(max_length=20)
    advisorEmail = models.CharField(max_length=20)


class Course(models.Model):
    courseCode = models.CharField(max_length=20)
    courseTitle = models.CharField(max_length=30)
    courseCredit= models.CharField(max_length=20)
    courseTeacher= models.ForeignKey(Advisor,on_delete=models.CASCADE)