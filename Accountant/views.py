from django.shortcuts import render
from django.urls import reverse

# Create your views here
from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView
from .models import Student


class AccountantHome(TemplateView):
        template_name="accountant/home.html"


class CreateStudent(CreateView):
        template_name="accountant/student_register.html"
        model=Student
        fields="__all__"

        def get_absolute_url(self):
            return reverse("newstudent")
class ListStudent(ListView):
    model=Student
    template_name="accountant/student_list.html"
    context_object_name="students"

        
