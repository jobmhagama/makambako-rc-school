from django.forms import modelForms
from .models import User


class NewUser():
    class Meta:
      model = User;
      fields= []