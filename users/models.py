from email.policy import default
from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    pass
    is_cit= models.BooleanField(max_length=10,default=False)
    is_lc=models.CharField(max_length=20),
    is_sv=models.CharField(max_length=20,default="No course")
    def __str_(self):
        return self.first_name