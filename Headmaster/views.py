from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView
from dataclasses import fields
from re import template
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView,CreateView,ListView,TemplateView
from django.views.generic.detail import DetailView
from Accountant.models import Student,StudentFee,StudentFoodFee,StudentFoodFee,StudentUniformFee,StudentTransportFee

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

#######Decoration for preventing un authenticated user to login without permmision

@method_decorator(login_required, name='dispatch')
class HeadmasterHome(TemplateView):
        template_name="headmaster/home.html"


@method_decorator(login_required, name='dispatch')
class AccountantHome(TemplateView):
        template_name="accountant/home.html"

@method_decorator(login_required, name='dispatch')
class CreateStudent(SuccessMessageMixin,CreateView):
        model=Student
        fields="__all__"
        template_name="headmaster/student_register.html"
        succes_message="New student has been created successfully"

@method_decorator(login_required, name='dispatch')     
class ListStudent(ListView):
    model=Student
    template_name="headmaster/student_list.html"
    context_object_name="students"

@method_decorator(login_required, name='dispatch')       
class CreateStudentFee(SuccessMessageMixin,CreateView):
        template_name="accountant/feePayment.html"
        model=StudentFee
        fields=['student','Payments','Cno',"amount",'year']
        success_message="Student fee was paid successfully"

@method_decorator(login_required, name='dispatch')
class CreateFoodFee(SuccessMessageMixin,CreateView):
        model=StudentFoodFee
        fields =["student","description",'amount','totalAmount']
        template_name="accountant/foodpayment.html"     
        success_message="Student fee was paid successfully"
        
@method_decorator(login_required, name='dispatch')
class CreateUniformFee(SuccessMessageMixin,CreateView):
        model=StudentUniformFee
        template_name="accountant/uniformpayment.html" 
        fields="__all__"
        success_message="Student fee for uniform was paid successfully"

@method_decorator(login_required, name='dispatch')
class CreateTransportFee(SuccessMessageMixin,CreateView):
        model=StudentTransportFee
        template_name="accountant/transportpayment.html"
        fields="__all__"
        success_message="Fee for transport was recorded successfully!!!"

@method_decorator(login_required, name='dispatch')
class FeeDetailView(TemplateView):
        template_name= "headmaster/feedetails.html"
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            id = self.kwargs["pk"]
            context["student"]=Student.objects.filter(pk=id)
            context["payments"] = StudentFee.objects.filter(student_id=id)
            return context
@method_decorator(login_required, name='dispatch')       
class FoodDetailView(TemplateView):
        template_name= "headmaster/student_food_details.html"
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            id = self.kwargs["pk"]
            context["student"]=Student.objects.filter(pk=id)
            context["payments"] = StudentFoodFee.objects.filter(student_id=id)
            return context

@method_decorator(login_required, name='dispatch')
class UniformDetailView(TemplateView):
        template_name= "headmaster/uniformdetails.html"
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            id = self.kwargs["pk"]
            context["student"]=Student.objects.filter(pk=id)
            context["payments"] = StudentUniformFee.objects.filter(student_id=id)
            return context

@method_decorator(login_required, name='dispatch')
class TransportDetailView(TemplateView):
        template_name= "headmaster/transportdetails.html"
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            id = self.kwargs["pk"]
            context["student"]=Student.objects.filter(pk=id)
            context["payments"] = StudentTransportFee.objects.filter(student_id=id)
            return context
            
@method_decorator(login_required, name='dispatch')
class HeadmasterDashboard(TemplateView):
        template_name="headmaster/dashboard.html"
   

# class PaymentDetails(TemplateView):
#         model= StudentFee
        

