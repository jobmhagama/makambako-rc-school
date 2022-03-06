from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView



class HeadmasterHome(TemplateView):
        template_name="headmaster/home.html"



