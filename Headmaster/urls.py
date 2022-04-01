from django.urls import path,include
from . import views

urlpatterns = [

     path("",views.HeadmasterDashboard.as_view(),name="headmaster_dashbaord"),
     path("Newstudent/",views.CreateStudent.as_view(),name="newstudentt"),
     path("students/",views.ListStudent.as_view(),name="Student_list"),
     path("studentfee/",views.CreateStudentFee.as_view(),name="Student_fee"),
     path("transportfee/",views.CreateTransportFee.as_view(),name="Student_transport"),
     path("transportdetails/<int:pk>",views.TransportDetailView.as_view(),name="Student_transport_details"),
     path("uniformfee/",views.CreateUniformFee.as_view(),name="Student_uniform"),
     path("student_uniform_detail/",views.UniformDetailView.as_view(),name="Student_uniform_detail"),
     path("foodfee/",views.CreateFoodFee.as_view(),name="Food_fee"),
     path("studentfee/<int:pk>",views.FeeDetailView.as_view(),name="Student_fee_detail"),
     path("studentfood/<int:pk>",views.FoodDetailView.as_view(),name="Student_food_detail"),
     path("studentdetail/<int:pk>",views.UniformDetailView.as_view(),name="Student_uniform_detail"),
]