from django.shortcuts import render
from assignment.models import Student, Faculty, Assignment, Question , Answer , StudyYear, Semester , Branch , Course
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return  render(request , 'index.html')

@login_required
def dashboard(request):
    return render(request , 'dashboard.html')


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
