from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate


def signin(request):
    if request.method =="POST" :
        username = request.POST["uname"]
        password = request.POST["pass"]
      
        user = authenticate(request,username=username,password=password)
        
        if user is not None and user.is_acc:
            login(request,user)
            print(user.username)
            return redirect('account')
        if user is not None and user.is_hm:
            login(request,user)
            return redirect("headmaster_dashbaord")
        else:
            messages.success(request,"invalid user name or password")
    return render(request,"registration/login.html")
    
def signout(request):
        logout(request)
        return render(request,"registration/login.html")

