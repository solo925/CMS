from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import *

## User Login Form (Applied in both student and teacher login)
class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username','password1','password2']
        widgets = {
                'username': forms.TextInput(),
                'password1': forms.PasswordInput(),
                'password2': forms.PasswordInput(),
                }
    
        

        
## Teacher Registration Form 
class TeacherProfileForm(forms.ModelForm):
    class Meta():
        model =  Teacher
        fields = ['name','unit_name','phone','email']
        widgets = {
                'name': forms.TextInput(),
                'subject_name': forms.TextInput(),
                'phone': forms.NumberInput(),
                'email': forms.EmailInput(),
                }

## Teacher Profile Update Form
# class TeacherProfileUpdateForm(forms.ModelForm):
#     class Meta():
#         model = Teacher
#         fields = ['name','subject_name','email','phone','teacher_profile_pic']

## Student Registration Form
class StudentProfileForm(forms.ModelForm):
    class Meta():
        model =  Student
        fields = ['name','admission_no','phone','email']
        widgets = {
                'name': forms.TextInput(),
                'admission_no': forms.NumberInput(),
                'phone': forms.NumberInput(),
                'email': forms.EmailInput(),
                }

        