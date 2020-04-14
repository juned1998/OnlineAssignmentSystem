from django import forms
from django.forms import ModelChoiceField
from .models import Student,Faculty,Branch,StudyYear,Course,Assignment,Question,Answer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from bootstrap_modal_forms.forms import BSModalForm


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




class CreateAssignmentForm(forms.ModelForm):
    course = forms.ModelChoiceField(queryset=None,empty_label=None,label = 'Please select course')
    deadline_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):   # no user here
        user = kwargs.pop('user', None)
        faculty = Faculty.objects.get(user = user)
        super(CreateAssignmentForm, self).__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.filter(faculty=faculty)

    class Meta:
        model = Assignment
        fields = ('number', 'course', 'deadline_date')


class AddAssignmentQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ['username','date','assignment']

class AddAssignmentAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        exclude = ['username','assignment','question','upvotes','similarity']
