from django.urls import path
from . import views

urlpatterns = [
    #path('',views.index,name='home')
    path('',views.QuestionListView.as_view(),name='index'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('question/<int:pk>', views.QuestionDetailView.as_view(), name='question-detail'),
    path('addCourse/', views.CourseCreate.as_view(), name='CreateCourse'),
    path('course/<int:pk>/update/', views.CourseUpdate.as_view(), name='UpdateCourse'),
    path('course/<int:pk>/delete/', views.CourseDelete.as_view(), name='DeleteCourse'),
    path('course_list/',views.CourseListView.as_view(),name='ViewCourse'),
    path('addAssignment/', views.AssignmentCreate.as_view(), name='CreateAssignment'),
    path('assignment_list/',views.AssignmentListView.as_view(),name='ViewAssignment'),
    path('assignment/<int:pk>/update/', views.AssigmentUpdate.as_view(), name='UpdateAssignment'),
    path('assignment/<int:pk>/delete/', views.AssignmentDelete.as_view(), name='DeleteAssignment'),
    path('assignment/<int:pk>', views.AssignmentDetailView.as_view(), name='assignment_detail'),
    path('addAssignmentQuestion/', views.QuestionCreateView.as_view(), name='CreateAssignmentQuestion'),
]
