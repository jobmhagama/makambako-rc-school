from dataclasses import fields
from re import template
from django.shortcuts import render
from django.urls import reverse

# Create your views here
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView,CreateView,ListView,TemplateView
from django.views.generic.detail import DetailView
from .models import StudentFee,StudentFoodFee,StudentFoodFee,StudentUniformFee,StudentTransportFee
from Headmaster.models import Student
##################Import forms
from .forms import *


class AccountantHome(TemplateView):
        template_name="accountant/home.html"


     
class ListStudent(ListView):
    model=Student
    template_name="accountant/student_list.html"
    context_object_name="students"

        
class CreateStudentFee(SuccessMessageMixin,CreateView):
        template_name="accountant/feePayment.html"
        model=StudentFee
        form_class=StudentFeeForm

        success_message="Student fee was paid successfully"

class CreateFoodFee(SuccessMessageMixin,CreateView):
        model=StudentFoodFee
        form_class=StudentFoodForm
        template_name="accountant/foodpayment.html"     
        success_message="Student fee was paid successfully"

class CreateUniformFee(SuccessMessageMixin,CreateView):
        model=StudentUniformFee
        template_name="accountant/uniformpayment.html" 
        form_class=StudentUniformForm
        success_message="Student fee for uniform was paid successfully"

class CreateTransportFee(SuccessMessageMixin,CreateView):
        model=StudentTransportFee
        form_class =StudentTransportForm
        template_name="accountant/transportpayment.html"
        success_message="Fee for transport was recorded successfully!!!"

class FeeDetailView(TemplateView):
        template_name= "accountant/feedetails.html"
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            id = self.kwargs["pk"]
            context["student"]=Student.objects.filter(pk=id)
            context["payments"] = StudentFee.objects.filter(student_id=id)
            return context
        
class FoodDetailView(TemplateView):
        template_name= "accountant/student_food_details.html"
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            id = self.kwargs["pk"]
            context["student"]=Student.objects.filter(pk=id)
            context["payments"] = StudentFoodFee.objects.filter(student_id=id)
            return context

class UniformDetailView(TemplateView):
        template_name= "accountant/uniformdetails.html"
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            id = self.kwargs["pk"]
            context["student"]=Student.objects.filter(pk=id)
            context["payments"] = StudentUniformFee.objects.filter(student_id=id)
            return context


class TransportDetailView(TemplateView):
        template_name= "accountant/transportdetails.html"
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            id = self.kwargs["pk"]
            context["student"]=Student.objects.filter(pk=id)
            context["payments"] = StudentTransportFee.objects.filter(student_id=id)
            return context

   

# class PaymentDetails(TemplateView):
#         model= StudentFee
        

