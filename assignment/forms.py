from django import forms
from django.forms import ModelChoiceField
from .models import Student,Faculty,Branch,StudyYear
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
#
# class StudentRegisterForm(forms.ModelForm):
#     branch = ModelChoiceField(queryset=Branch.objects.all())
#     year = ModelChoiceField(queryset=StudyYear.objects.all())
#     class Meta:
#         model = Student
#         fields = ['rollnumber', 'branch', 'year']
#
# class FacultyRegisterForm(forms.ModelForm):
#     branch = ModelChoiceField(queryset=Branch.objects.all())
#     class Meta:
#         model = Faculty
#         fields = ['code', 'branch']

class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(max_length= 50)
    last_name = forms.CharField(max_length = 50)
    class Meta :
        model = User
        fields = ('username','email','first_name','last_name','password1','password2')

    def save(self , commit = True):
        user = super().save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user

class StudentSignUpForm(forms.ModelForm):
    branch = ModelChoiceField(queryset=Branch.objects.all())
    year = ModelChoiceField(queryset=StudyYear.objects.all())
    class Meta :
        model = Student
        fields = ('rollnumber','branch','year')

class FacultySignUpForm(forms.ModelForm):
    branch = ModelChoiceField(queryset=Branch.objects.all())
    class Meta :
        model = Faculty
        fields = ('code','branch')
