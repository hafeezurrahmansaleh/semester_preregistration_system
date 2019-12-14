from django.db import models
from users.models import User
# Create your models here.


class TeacherInfo(models.Model):
    tID = models.CharField(max_length=30,unique=True)
    tName = models.CharField(max_length=30)
    tInitial = models.CharField(max_length=10)
    tDesignation = models.CharField(max_length=20)
    tPhone = models.CharField(max_length=20)
    tEmail = models.CharField(max_length=20)