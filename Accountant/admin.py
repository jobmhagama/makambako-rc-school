import site
from django.contrib import admin
from .models import Student,StudentFee,StudentFoodFee,StudentUniformFee,StudentTransportFee

# Register your models here.

admin.site.register(Student)
admin.site.register(StudentFee)
admin.site.register(StudentFoodFee)
admin.site.register(StudentUniformFee)
admin.site.register(StudentTransportFee)
