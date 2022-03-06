
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from . import models

# Create your views here.
def home(request):
    return render(request,"web/home.html")

def index(request):
    return render(request,"web/index.html")
def login(request):
    return render(request,"registration/login.html")
def register(request):
    if request.method == "POST":
        fname  = request.POST["fname"]
        mname  = request.POST["mname"]
        lname  = request.POST["lname"]
        password = request.POST["password"]
        email = request.POST["email"]
        username =request.POST["username"]
        user= models.User
        user.objects.create_user(first_name=fname,last_name=lname,email=email,password=password,username=username,is_acc=True)
        messages.success(request,"Your Account has been created successfully!")
        return redirect("register")
    return render(request,"web/register.html")





