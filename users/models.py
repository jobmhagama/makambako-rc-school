from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    #This is the accountant
    is_acc= models.BooleanField(max_length=10,default=False)
    #This is the headmaster
    is_hm =models.BooleanField(max_length=10,default=False)
    def __str_(self):
        return self.first_name