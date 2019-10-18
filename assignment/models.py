from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
#if hasattr(self, 'student'):


class StudyYear(models.Model):
    year = models.CharField(max_length = 50 , help_text = "Enter in this format First Year , Second Year, etc.")

    def __str__(self):
        return self.year

class Semester(models.Model):
    sem = models.IntegerField()

    def __str__(self):
        return f'semester {self.sem}'


class Branch(models.Model):
    name = models.CharField(max_length = 50 , help_text = "Example Computer Engineering")

    def __str__(self):
        return self.name

class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete =models.CASCADE)
    branch = models.ForeignKey(Branch , on_delete = models.SET_NULL,null=True)
    code = models.CharField(max_length=30 ,blank = True, unique = True)
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class Student(models.Model):
    user = models.OneToOneField(User , on_delete =models.CASCADE)
    rollnumber = models.CharField(max_length = 10)
    branch = models.ForeignKey(Branch , on_delete = models.SET_NULL , null=True)
    year = models.ForeignKey(StudyYear , on_delete = models.SET_NULL , null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class Course(models.Model):
    name = models.CharField(max_length = 50)
    branch = models.ForeignKey(Branch,on_delete = models.SET_NULL,blank=True,null=True)
    faculty = models.ForeignKey(Faculty ,on_delete = models.SET_NULL,blank=True,null=True)
    year = models.ForeignKey(StudyYear ,on_delete = models.SET_NULL,blank=True,null=True)
    semester = models.ForeignKey(Semester ,on_delete = models.SET_NULL,blank=True,null=True )

    def __str__(self):
        return self.name
    # def get_absolute_url(self):
    #     """Returns the url to access a detail record for this book."""
    #     return reverse('course-detail', args=[str(self.id)])

class Assignment(models.Model):
    number = models.IntegerField()
    course = models.ForeignKey(Course,on_delete = models.SET_NULL,blank=True,null=True)
    publish_date = models.DateField(auto_now_add = True)
    deadline_date = models.DateField()
    faculty = models.ForeignKey(Faculty,on_delete = models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return f'Assignment {self.number}-{self.course}'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this Assignment."""
        return reverse('assignment-detail', args=[str(self.id)])

class Question(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.SET_NULL,blank=True,null=True)
    username = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    title = models.CharField(max_length = 200)
    description = models.TextField(blank=True , null = True)
    marks = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('question-detail', args=[str(self.id)])

class Answer(models.Model):
    STATUS = [('Draft','Draft'),('Published','Published')]
    question = models.ForeignKey(Question,on_delete = models.CASCADE)
    answer_txt = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=12,choices=STATUS,default='Draft')
    username = models.ForeignKey(User,on_delete = models.SET_NULL,null=True)

    def __str__(self):
        return f'{self.question.title} by {self.username.first_name}'
