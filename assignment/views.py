from django.shortcuts import render, redirect
from .models import Student, Faculty, Assignment, Question , Answer , StudyYear, Semester , Branch , Course
from django.contrib.auth.decorators import login_required
from .forms import ExtendedUserCreationForm,StudentSignUpForm,FacultySignUpForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.
def index(request):
    return  render(request , 'index.html')

@login_required
def dashboard(request):
    return render(request , 'dashboard/index.html')


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

# def StudentRegister(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         s_reg_form = StudentRegisterForm(request.POST)
#     if form.is_valid() and s_reg_form.is_valid():
#         user = form.save()
#         user.refresh_from_db()  # load the profile instance created by the signal
#         s_reg_form = StudentRegisterForm(request.POST, instance=user.profile)
#         s_reg_form.full_clean()
#         s_reg_form.save()
#         messages.success(request, f'Your account has been sent for approval!')
#         return redirect('login')
#     else:
#         form = UserRegisterForm()
#         s_reg_form = StudentRegisterForm()
#         context = {
#             'form': form,
#             's_reg_form': s_reg_form
#         }
#     return render(request, 'StudentRegister.html', context)
#
# def FacultyRegister(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         f_reg_form = FacultyRegisterForm(request.POST)
#     else:
#         form = 'dummyString'
#     if form.is_valid() and f_reg_form.is_valid():
#         user = form.save()
#         user.refresh_from_db()  # load the profile instance created by the signal
#         f_reg_form = FacultyRegisterForm(request.POST, instance=user.profile)
#         f_reg_form.full_clean()
#         f_reg_form.save()
#         messages.success(request, f'Your account has been sent for approval!')
#         return redirect('login')
#     else:
#         form = UserRegisterForm()
#         s_reg_form = StudentRegisterForm()
#         context = {
#             'form': form,
#             's_reg_form': s_reg_form
#         }
#     return render(request, 'StudentRegister.html', context)

# def StudentSignUpForm(request):
#     if request.method == 'POST':
#         form = ExtendedUserCreationForm(request.POST)
#         student_form = StudentSignUpForm(request.POST)
#
#         if form.is_valid() and student_form.is_valid():
#             user = form.save()
#             student = student_form.save(commit=False)
#             student.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username = username , password = password)
#             login(request,user)
#             return redirect('index')
#     else:
#         form = ExtendedUserCreationForm(request.POST)
#         student_form = StudentSignUpForm(request.POST)
#     context = {'form': form , 'student_form':student_form}

def registerView(request):
    return render(request , 'registration/register.html')


class CourseCreate(CreateView):
    model = Course
    template_name = 'dashboard/course.html'
    fields = ['name' , 'branch','year','semester']
    def form_valid(self, form):
        faculty = Faculty.objects.get(user=self.request.user)
        form.instance.faculty = faculty
        return super(CourseCreate, self).form_valid(form)

class CourseListView(generic.ListView):
    model = Course
    template_name = "dashboard/course_list.html"
    context_object_name = 'course_list'
    paginate_by = 10
    def get_queryset(self):
        faculty = Faculty.objects.get(user=self.request.user)
        return Course.objects.filter(faculty=faculty)
