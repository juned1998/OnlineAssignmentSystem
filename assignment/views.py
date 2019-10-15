from django.shortcuts import render, redirect
from .models import Student, Faculty, Assignment, Question , Answer , StudyYear, Semester , Branch , Course
from django.contrib.auth.decorators import login_required
from .forms import ExtendedUserCreationForm,StudentSignUpForm,FacultySignUpForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.urls import reverse_lazy
# Create your views here.
def index(request):
    return  render(request , 'index.html')

@login_required
def FacultyDashboard(request):
    return render(request , 'Faculty_Dashboard/index.html')


def FacultyRegistration(request):
    if request.method == "POST":
        if request.POST['pass'] == request.POST['passwordagain']:
            try:
                user = User.objects.get(username = request.POST['uname'])
                return render(request, 'registration/FacultyRegistration.html',{'error':"Username already exists"})
            except User.DoesNotExist:
                user = User.objects.create_user(username = request.POST['uname'] , password=request.POST['pass'])
                auth.login(request,user)
                return HttpResponse("Signed Up !")
        else:
            return render(request , 'register.html' , {'error' : "Password doesn't Match !"})
    else:
        return render(request,'registration/FacultyRegistration.html')

from django.views import generic
class QuestionListView(generic.ListView):
    model = Question
    template_name = 'index.html'
    paginate_by = 10
    def get_queryset(self):
        return Question.objects.order_by('-date')


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
    template_name = 'Faculty_Dashboard/add_course.html'
    fields = ['name' , 'branch','year','semester']
    def form_valid(self, form):
        faculty = Faculty.objects.get(user=self.request.user)
        form.instance.faculty = faculty
        return super(CourseCreate, self).form_valid(form)
    def get_success_url(self):
        return reverse('ViewCourse')

class CourseUpdate(UpdateView):
    model = Course
    template_name = 'Faculty_Dashboard/add_course.html'
    fields = ['name' , 'branch','year','semester']
    def form_valid(self, form):
        faculty = Faculty.objects.get(user=self.request.user)
        form.instance.faculty = faculty
        return super(CourseUpdate, self).form_valid(form)
    def get_success_url(self):
        return reverse('ViewCourse')

class CourseDelete(DeleteView):
    model = Course
    template_name = "Faculty_Dashboard/course_list.html"
    success_url = reverse_lazy('ViewCourse')
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

class CourseDetailView(generic.DetailView):
    model = Course
    template_name = "Faculty_Dashboard/course_detail.html"


class CourseListView(generic.ListView):
    model = Course
    template_name = "Faculty_Dashboard/course_list.html"
    context_object_name = 'course_list'
    paginate_by = 10
    def get_queryset(self):
        faculty = Faculty.objects.get(user=self.request.user)
        return Course.objects.filter(faculty=faculty)

from .forms import CreateAssignmentForm
class AssignmentCreate(CreateView):
    model = Assignment
    form_class = CreateAssignmentForm
    template_name = 'Faculty_Dashboard/add_assignment.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        faculty = Faculty.objects.get(user=self.request.user)
        form.instance.faculty = faculty
        return super(AssignmentCreate, self).form_valid(form)
    def get_success_url(self):
        return reverse('ViewAssignment')

class AssigmentUpdate(UpdateView):
    model = Assignment
    form_class = CreateAssignmentForm
    template_name = 'Faculty_Dashboard/add_assignment.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        faculty = Faculty.objects.get(user=self.request.user)
        form.instance.faculty = faculty
        return super(AssigmentUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse('ViewAssignment')

class CourseAssigmentUpdate(UpdateView):
    model = Assignment
    form_class = CreateAssignmentForm
    template_name = 'Faculty_Dashboard/add_assignment.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        faculty = Faculty.objects.get(user=self.request.user)
        form.instance.faculty = faculty
        return super(CourseAssigmentUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('course_detail', kwargs={'pk': self.object.course_id})


class AssignmentListView(generic.ListView):
    model = Assignment
    template_name = "Faculty_Dashboard/assignment_list.html"
    context_object_name = 'assignment_list'
    paginate_by = 10
    def get_queryset(self):
        faculty = Faculty.objects.get(user=self.request.user)
        return Assignment.objects.filter(faculty=faculty)

class AssignmentDelete(DeleteView):
    model = Assignment
    template_name = "Faculty_Dashboard/assignment_list.html"
    success_url = reverse_lazy('ViewAssignment')
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

#Returns to Course Assignment list after deleting
class CourseAssignmentDelete(DeleteView):
    model = Assignment
    template_name = "Faculty_Dashboard/course_detail.html"
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    def get_success_url(self):
        return reverse_lazy('course_detail', kwargs={'pk': self.object.course_id})

class AssignmentDetailView(generic.DetailView):
    model = Assignment
    template_name = "Faculty_Dashboard/assignment_detail.html"


from django.shortcuts import get_object_or_404
from .forms import AddAssignmentQuestionForm
def QuestionCreate(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    if request.method == 'POST':
        form = AddAssignmentQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.assignment = assignment
            question.save()
            return redirect('assignment_detail', assignment.pk)
    else:
        form = AddAssignmentQuestionForm()
    return render(request, 'Faculty_Dashboard/add_question.html', {'quiz': assignment, 'form': form ,'pk': assignment.id })

def QuestionUpdate(request, question_pk , assignment_pk):
    assignment = get_object_or_404(Assignment, pk=assignment_pk)
    question = get_object_or_404(Question, pk=question_pk)
    if request.method == 'POST':
        form = AddAssignmentQuestionForm(request.POST , instance = question )
        if form.is_valid():
            form.save()
            return redirect('assignment_detail',assignment.id)
    else:
        form = AddAssignmentQuestionForm(instance=question)
    return render(request, 'Faculty_Dashboard/update_question.html', {'quiz': assignment,'question':question,'form': form})





class QuestionDeleteView(DeleteView):
    model = Question
    template_name = "Faculty_Dashboard/assignment_detail.html"
    # success_url = reverse_lazy('assignment_detail', kwargs={'pk': self.object.assignment_id})
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    def get_success_url(self):
        return reverse_lazy('assignment_detail', kwargs={'pk': self.object.assignment_id})



############# Student Dashboard ######################################################################################################################
@login_required
def StudentDashboard(request):
    return render(request , 'Student_Dashboard/index.html')
