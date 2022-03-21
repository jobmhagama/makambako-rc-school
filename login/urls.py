from . import views
from django.contrib import admin
from django.urls import path,include


urlpatterns = [

  path("signin/",views.signin,name="signin"),
  path("signout/",views.signout,name="signout"),
  #After a successfullly login users will be directed towards their account from here
  path('account/', include("Accountant.urls")),
  #This for headmaster
  path('headmaster/', include("Headmaster.urls")),

]