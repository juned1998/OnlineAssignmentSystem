from django.shortcuts import render, redirect
from .forms import CourseForm
from .models import Student, Faculty, Assignment, Question , Answer , StudyYear, Semester , Branch , Course
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return  render(request , 'index.html')

@login_required
def dashboard(request):
    return render(request , 'dashboard/blank.html')


from django.views import generic
class QuestionListView(generic.ListView):
    model = Question
    template_name = 'index.html'
    paginate_by = 10

    def get_queryset(self):
        return Question.objects.all()

class QuestionDetailView(generic.DetailView):
    model = Question

def login(request):
    return render(request , 'login.html')

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class CourseListView(generic.ListView):
    model = Course

class CourseCreate(CreateView):
    model = Course
    fields = '__all__'

class CourseUpdate(UpdateView):
    model = Course
    fields = '__all__'

class CourseDelete(DeleteView):
    model = Course
    success_url = reverse_lazy('course')

class CourseDetailView(generic.DetailView):
    model = Course




def emp(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('show')
            except:
                pass
    else:
        form = CourseForm()
    return render(request,'index.html',{'form':form})

def show(request):
    courses = Course.objects.all()
    return render(request,'show.html',{'courses':courses})

def edit(request, id):
    course = Course.objects.get(id=id)
    return render(request,'edit.html', {'course':course})

def update(request, id):
    course = Course.objects.get(id=id)
    form = CourseForm(request.POST, instance = course)
    if form.is_valid():
        form.save()
        return redirect("show")
    return render(request, 'edit.html', {'course': course})

def destroy(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect("show")
