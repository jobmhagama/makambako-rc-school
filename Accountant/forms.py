from curses import meta
from dataclasses import field
from lib2to3.pgen2.token import EQUAL
from operator import eq
from pyexpat import model
from signal import raise_signal
from django import forms
from .models import *

class CreateStudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"

class StudentFoodForm(forms.ModelForm):
    class Meta:
        model=StudentFoodFee
        fields="__all__"
    def clean(self):
        data=super().clean()
        description=data.get("description")
        amount=data.get("amount")
        totalAmount=data.get("totalAmount'")
        
        if len(description) > 1000:
            raise forms.ValidationError("The description is to large")
        elif description.isdigit():
            raise forms.ValidationError("The description cant be a number")
        elif (amount !=  totalAmount) is True:
            raise forms.ValidationError("amount and total amount does match")
        elif amount>10000000:
            raise forms.ValidationError("please enter  correct amount")
class StudentTransportForm(forms.ModelForm):
        class Meta:
            model=StudentTransportFee
            fields="__all__"

        def clean(self):
            cleaned_data=super().clean()
            cno=cleaned_data["Cno"]
            description=cleaned_data["description"]
            amount=cleaned_data["amount"]
            if amount>10000000:
                raise forms.ValidationError("The amount is too large")
            elif len(description) >100: 
                raise forms.ValidationError("description is too large")
            elif description.isdigit():
                 raise forms.ValidationError("The description cant be a number")

            #if cno.isdigit():
                #raise forms.ValidationError("invalid control number")

           # elif len(cno)<7:
               # raise forms.ValidationError("incorrect controll number")
           # elif 'RC' not in cno:
               # raise forms.ValidationError("control number is not correct")
           # elif len(description)>100:
                # raise forms.ValidationError("The description is to large")
           
class StudentUniformForm(forms.ModelForm):  
        class Meta:
            model= StudentUniformFee
            fields="__all__"
        def clean(self):
            cleaned_data=super().clean()
            description=cleaned_data["description"]
            amount=cleaned_data["amount"]
            if description.isdigit():
                 raise forms.ValidationError("The description cant be a number")
            elif len(description)>100:
                 raise forms.ValidationError("description provided is too large")
            elif amount>1000000:
                 raise forms.ValidationError("The amount is too large")

       
    
class StudentFeeForm(forms.ModelForm):
    class Meta:
        model=StudentFoodFee
        fields="__all__"
    def clean(self):
        data=super(self).clean()

