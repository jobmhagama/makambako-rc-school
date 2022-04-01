from django import forms
from . models import *
class CreateStudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
