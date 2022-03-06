from django.db import models
from django.urls import reverse
# Create your models here.


class Student(models.Model):
    First_Name=models.CharField(default="Job",max_length=20)
    Middle_Name=models.CharField(default="Job",max_length=20)
    Last_Name=models.CharField(default="Job",max_length=20)
    Parent_Name =models.CharField(default="Job",max_length=20)
    Parent_Occupation=models.CharField(default="Job",max_length=20)
    parent_Education=models.CharField(default="Job",max_length=20)
    ParentAddress=models.CharField(default="Job",max_length=20)
    Birthd_Date=models.CharField(default="Job",max_length=20)
    Local=models.CharField(default="Job",max_length=20)
    Description=models.TextField(default="Job",max_length=20)
    Nida_Number=models.CharField(default="Job",max_length=20)
    Birthd_Certificate=models.CharField(default="Job",max_length=20)
    phone=models.CharField(default="Job",max_length=20)

    def get_absolute_url(self):
            return reverse("newstudent")

