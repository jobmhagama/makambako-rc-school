from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    First_Name=models.CharField(default="eg Alex",max_length=20)
    Middle_Name=models.CharField(default="James",max_length=20)
    Last_Name=models.CharField(default="Mtaho",max_length=20)
    Parent_Name =models.CharField(default="Alex",max_length=20)
    Parent_Occupation=models.CharField(default="eg.Mkulima",max_length=20)
    parent_Education=models.CharField(default="standard seven",max_length=20)
    ParentAddress=models.CharField(default="Dodoma",max_length=20)
    Birthd_Date=models.DateField()
    Local=models.CharField(default="mtaa",max_length=20)
    Description=models.TextField(default="Description related to a kid",max_length=20)
    Nida_Number=models.CharField(default="7838373388UD",max_length=20)
    Birthd_Certificate=models.CharField(default="8383773738WJJJW",max_length=20)
    phone=models.CharField(default="0786976118",max_length=20)
    def __str__(self):
        return self.First_Name

    def get_absolute_url(self):
            return reverse("newstudentt")