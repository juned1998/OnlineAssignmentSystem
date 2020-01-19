from django.shortcuts import render, redirect,HttpResponse
from .models import Student, Faculty, Assignment, Question , Answer , StudyYear, Semester , Branch , Course
from django.contrib.auth.decorators import login_required
from .forms import ExtendedUserCreationForm,StudentSignUpForm,FacultySignUpForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.db.models import Count
from django.core import serializers
# Create your views here.
def index(request):
    years  = StudyYear.objects.all()
    branchs= Branch.objects.all()
    return  render(request , 'index.html', {'years':year , 'branchs':branchs} )

def filter(request):
    if(request.method=="GET"):
        branch = request.GET['branchfilter']
        year = request.GET['yearfilter']
        course = request.GET['coursefilter']

        course = Course.objects.filter(name=course,branch=branch,year=year)
        assignemnt=Assignemnt.objects.filter(course=course)
        questions=Question.objects.filter(assignment=assignemnt)
        return render(request,"index.html",{'question_list':questions})



@login_required
def FacultyDashboard(request):
    return render(request , 'Faculty_Dashboard/index.html')



def FacultyRegistration(request):
    if request.method == "POST":
        if request.POST['pass'] == request.POST['passwordagain']:
            try:
                user = User.objects.get(username = request.POST['uname'])
                return render(request, 'registration/FacultyRegistration.html',{'error':"Username already exists"})
                faculty = Faculty.objects.get( code = request.POST['FacultyCode'])
                return render(request, 'registration/FacultyRegistration.html',{'error':"Faculty Code already exists"})
            except User.DoesNotExist:
                user = User.objects.create_user(username = request.POST['uname'] , password=request.POST['pass'] ,first_name =request.POST['firstName'],last_name = request.POST['lastName'],email=request.POST['email'] )
                branchName = request.POST['FacultyBranch']
                branch = Branch.objects.get(name = branchName)
                code = request.POST['FacultyCode']
                newFaculty = Faculty(user= user ,branch = branch , code = code )
                newFaculty.save()
                # login(user)
                return render(request ,'registration/FacultyRegistration.html' , {'message' : "Registration succesful please login !"})
        else:
            branch = Branch.objects.all()
            return render(request , 'registration/FacultyRegistration.html' , {'error' : "Password doesn't Match !" , "branchs" : branch})
    else:
        branch = Branch.objects.all()
        return render(request,'registration/FacultyRegistration.html',{"branchs":branch})


def StudentRegistration(request):
    if request.method == "POST":
        if request.POST['pass'] == request.POST['passwordagain']:
            try:
                user = User.objects.get(username = request.POST['uname'])
                return render(request, 'registration/StudentRegistration.html',{'error':"Username already exists"})
                student = Student.objects.get( code = request.POST['rollnumber'])
                return render(request, 'registration/FacultyRegistration.html',{'error':"Rollnumber already exists"})
            except User.DoesNotExist:
                user = User.objects.create_user(username = request.POST['uname'] , password=request.POST['pass'] ,first_name =request.POST['firstName'],last_name = request.POST['lastName'],email=request.POST['email'] )
                year = request.POST['studentYear']
                year = StudyYear.objects.get(year = year)
                branchName = request.POST['studentBranch']
                branch = Branch.objects.get(name = branchName)
                rollnumber = request.POST['rollnumber']
                newStudent = Student(user= user ,branch = branch ,year = year , rollnumber = rollnumber )
                newStudent.save()
                # login(user)
                return render(request ,'registration/StudentRegistration.html' , {'message' : "Registration succesful please login !"})
        else:
            branch = Branch.objects.all()
            year = StudyYear.objects.all()
            return render(request , 'registration/StudentRegistration.html' , {'error' : "Password doesn't Match !" , "branchs" : branch,"years":year})
    else:
        branch = Branch.objects.all()
        year = StudyYear.objects.all()
        return render(request,'registration/StudentRegistration.html',{"branchs":branch,"years":year})


from django.views import generic
class QuestionListView(generic.ListView):
    model = Question
    template_name = 'index.html'
    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['branchs'] = Branch.objects.all()
        context['years'] = StudyYear.objects.all()
        context['courses']=Course.objects.all()
        return context
    def get_queryset(self):
        return Question.objects.order_by('-date')


class RepoQuestionDetailView(generic.DetailView):
    model = Question
    template_name = "questionAllAnswers.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['answers'] = self.object.answer_set.all().annotate(count=Count('upvotes')).order_by('-count')
        return context

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
    template_name = 'Faculty_Dashboard/update_assignment.html'

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
    return render(request, 'Faculty_Dashboard/add_question.html', {'assignment': assignment, 'form': form ,'pk': assignment.id })


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
    return render(request, 'Faculty_Dashboard/update_question.html', {'assignment': assignment,'question':question,'form': form})





class QuestionDeleteView(DeleteView):
    model = Question
    template_name = "Faculty_Dashboard/assignment_detail.html"
    # success_url = reverse_lazy('assignment_detail', kwargs={'pk': self.object.assignment_id})
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    def get_success_url(self):
        return reverse_lazy('assignment_detail', kwargs={'pk': self.object.assignment_id})

def getSubmittedAnswer(request , id):
    question = get_object_or_404(Question, pk=id)
    answers = Answer.objects.filter(question = question , status = 'Published')
    return render(request, 'Faculty_Dashboard/submitted_answers.html', {'question': question, 'answers':answers })

def rejectAnswer(request , qid,ansID ):
    question = get_object_or_404(Question, pk=qid)
    answers = Answer.objects.filter(question = question , status = 'Published')
    answer = get_object_or_404(Answer , pk =ansID)
    answer.status = 'Draft'
    answer.save()
    return render(request, 'Faculty_Dashboard/submitted_answers.html', {'question': question, 'answers':answers })

def questionBank(request):
    faculty = Faculty.objects.get(user=request.user)
    courses  = Course.objects.filter(faculty=faculty)
    return  render(request , 'Faculty_Dashboard/question_bank.html', {'courses':courses})

def all_json_models(request, id):
    course = Course.objects.get(id=id)
    assignments = Assignment.objects.all().filter(course=course)
    json_models = serializers.serialize("json", assignments)
    return HttpResponse(json_models, content_type="application/javascript")

def generateQB(request):
    if(request.method=="GET"):
        course = request.GET['course']
        assignmentList = request.GET.getlist('assignment')
        course = Course.objects.get(id=course)
        assignment=Assignment.objects.filter(course=course,id__in=assignmentList)
        questions=Question.objects.filter(assignment__in=assignment)
        faculty = Faculty.objects.get(user=request.user)
        courses  = Course.objects.filter(faculty=faculty)
        return render(request,"Faculty_Dashboard/question_bank.html",{'question_list':questions,'courses': courses})


############# Student Dashboard ######################################################################################################################
@login_required
def StudentDashboard(request):
    return render(request , 'Student_Dashboard/index.html')

class StudentCourseListView(generic.ListView):
    model = Course
    template_name = "Student_Dashboard/course_list.html"
    context_object_name = 'course_list'
    paginate_by = 10
    def get_queryset(self):
        student = Student.objects.get(user = self.request.user)
        branch = Branch.objects.get(name=student.branch.name)
        year = StudyYear.objects.get(year=student.year)
        return Course.objects.filter(branch=branch,year=year)

class StudentAssignmentListView(generic.ListView):
    model = Assignment
    template_name = "Student_Dashboard/assignment_list.html"
    context_object_name = 'assignment_list'
    paginate_by = 10
    def get_queryset(self):
        student = Student.objects.get(user = self.request.user)
        branch = Branch.objects.get(name=student.branch)
        year = StudyYear.objects.get(year=student.year)
        return Assignment.objects.filter(course__year= year,course__branch=branch)

class StudentCourseDetailView(generic.DetailView):
    model = Course
    template_name = "Student_Dashboard/course_detail.html"

class StudentAssignmentDetailView(generic.DetailView):
    model = Assignment
    template_name = "Student_Dashboard/assignment_detail.html"
    def get_context_data(self, **kwargs):
        context = super(StudentAssignmentDetailView, self).get_context_data(**kwargs)
        answers = Answer.objects.filter(username = self.request.user)
        context['answers'] = answers
        return context

from .forms import AddAssignmentAnswerForm
def AnswerCreate(request, pk):
    question = get_object_or_404(Question, pk=pk)
    user_answer = Answer.objects.filter(question = question, username = request.user).first()
    if request.method == 'POST':
        form = AddAssignmentAnswerForm(request.POST)

        if form.is_valid():
            answer = request.POST['answer_txt']
            status = request.POST['status']
            userAnswer, created = Answer.objects.get_or_create(username=request.user, question = question )
            userAnswer.answer_txt = answer
            userAnswer.status = status
            userAnswer.save()
            return redirect('student_assignment_detail', question.assignment.id)
    elif user_answer:
        form = AddAssignmentAnswerForm(instance = user_answer)
    else:
        form = AddAssignmentAnswerForm()
    return render(request, 'Student_Dashboard/add_answer.html', {'question': question, 'form': form ,'pk': question.assignment.id , 'cpk': question.assignment.course.id  })

def getAnswer(request,pk,apk):
    assignment = get_object_or_404(Assignment,pk=apk)
    question = get_object_or_404(Question,pk=pk)
    answer = get_object_or_404(Answer,question=question,username=request.user)
    return render(request, 'Student_Dashboard/answer_detail.html', {'question': question, 'answer':answer , 'assignment': assignment  })


# class StudentAnswerDetailView(generic.DetailView):
#     model = Answer
#     template_name = "Student_Dashboard/answer_detail.html"
#
# class StudentQuestionDetailView(generic.DetailView):
#     model = Question
#     template_name = "Student_Dashboard/question_detail.html"
