from django.urls import path,include
from . import views

urlpatterns =[
    path("",views.AccountantHome.as_view(),name="account"),
     path("newstudent/",views.CreateStudent.as_view(),name="newstudent"),
     path("studentfee/",views.CreateStudentFee.as_view(),name="student_fee"),
     path("transportfee/",views.CreateTransportFee.as_view(),name="student_transport"),
     path("transportdetails/<int:pk>",views.TransportDetailView.as_view(),name="student_transport_details"),
     path("uniformfee/",views.CreateUniformFee.as_view(),name="student_uniform"),
     path("student_uniform_detail/",views.UniformDetailView.as_view(),name="  student_uniform_detail"),
     path("foodfee/",views.CreateFoodFee.as_view(),name="food_fee"),
     path("studentfee/<int:pk>",views.FeeDetailView.as_view(),name="student_fee_detail"),
     path("studentfood/<int:pk>",views.FoodDetailView.as_view(),name="student_food_detail"),
     path("studentdetail/<int:pk>",views.UniformDetailView.as_view(),name="student_uniform_detail"),
     path("students/",views.ListStudent.as_view(),name="student_list")
]