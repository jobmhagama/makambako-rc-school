from datetime import date
from random import choices
from tokenize import Double
from django.db import models
from django.urls import reverse
# Create your models here.
from Headmaster.models import Student
class StudentFee(models.Model):
    PAYMENTS = [
    ('Payments', (('1st quarter', '1st qurter'),
    ('2nd quarter', '2st qurter'),
    ('3rd quarter', '3rd qurter'),
    ('4th quarter', '4th qurter'),
    
     )),
    
    ]
    student =models.ForeignKey(Student,on_delete=models.CASCADE)
    Payments= models.CharField(
        max_length=32,
         choices=PAYMENTS,
          default='available',
        )
    amount=models.FloatField(default=200000.000)
    Cno=models.CharField(max_length=50)
    created_at=models.DateField(auto_now=True, auto_now_add=False) 
    year= models.PositiveSmallIntegerField(blank=True, null=True)
    def __str__(self) -> str:
        return self.student
    def get_absolute_url(self):
            return reverse("student_fee")

class StudentFoodFee(models.Model):
     student =models.ForeignKey(Student,on_delete=models.CASCADE)
     date=models.DateField(auto_now_add=True)
     description=models.TextField(max_length=2000)
     amount=models.IntegerField()
     totalAmount=models.IntegerField(null=True)
     def __str__(self) -> str:
         return  self.student
     def get_absolute_url(self):
            return reverse("food_fee")

            

class StudentUniformFee(models.Model):
     student =models.ForeignKey(Student,on_delete=models.CASCADE)
     Cno=models.IntegerField()
     Shirt=models.BooleanField()
     trouser=models.BooleanField()
     gawon=models.BooleanField
     sweater=models.BooleanField()
     Cap=models.BooleanField()
     tracksuit=models.BooleanField()
     date=models.DateField(auto_now_add=True)
     description=models.TextField(max_length=2000)
     amount=models.IntegerField()
     def __str__(self):
         return  self.student.First_Name
     def get_absolute_url(self):
            return reverse("student_uniform")


            
class StudentTransportFee(models.Model):
     student =models.ForeignKey(Student,on_delete=models.CASCADE)
     PAYMENTS = [
         ('Payments', (('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
         ('April', 'Appril'),
    
        )),
    
        ]
     month = models.CharField(max_length=50,choices=PAYMENTS,default="January")
     Cno=models.IntegerField()
     amount=models.FloatField()
     description=models.TextField()
     datepaid=models.DateField(auto_created=True,auto_now_add=True)

     def get_absolute_url(self):
            return reverse("student_transport")
     def __str__(self):
         return self.student.First_Name