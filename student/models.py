from django.db import models
from teacher.models import TeacherInfo
# Create your models here.


class StudentInfo(models.Model):
    stID = models.CharField(max_length=20, unique=True)
    stName = models.CharField(max_length=30)
    stEmail = models.CharField(max_length=30)
    stGender = models.CharField(max_length=6)
    stPhone = models.CharField(max_length=20)
    stAdvisor = models.ForeignKey( TeacherInfo, on_delete=models.CASCADE,null=True)

