import imp
from pickle import NONE
from traceback import print_tb
from click import echo
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate

def signin(request):
    if request.method =="POST" :
        username = request.POST["uname"]
        password = request.POST["pass"]
        print(username)
        user = authenticate(request,username=username,password=password)

        if user is not None and user.is_student:
            users = user.is_student
            print(users)
            login(request,user)
            return redirect("home")
    return render(request,"registration/login.html")


