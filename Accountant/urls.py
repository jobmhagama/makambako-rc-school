from django.urls import path,include
from . import views

urlpatterns =[
    path("",views.AccountantHome.as_view(),name="account"),
     path("newstudent/",views.CreateStudent.as_view(),name="newstudent"),
     path("students/",views.ListStudent.as_view(),name="student_list")
]