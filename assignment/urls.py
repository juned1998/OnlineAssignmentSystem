from django.urls import path
from . import views

#faculty dashboard
urlpatterns = [
    #path('',views.index,name='home')
    path('FacultyRegistration/',views.FacultyRegistration,name='FacultyRegistration'),
    path('',views.QuestionListView.as_view(),name='index'),
    path('FacultyDashboard',views.FacultyDashboard,name='FacultyDashboard'),
    path('question/<int:pk>', views.QuestionDetailView.as_view(), name='question-detail'),
    path('addCourse/', views.CourseCreate.as_view(), name='CreateCourse'),
    path('course/<int:pk>/update/', views.CourseUpdate.as_view(), name='UpdateCourse'),
    path('course/<int:pk>/delete/', views.CourseDelete.as_view(), name='DeleteCourse'),
    path('course/<int:pk>', views.CourseDetailView.as_view(), name='course_detail'),
    path('course_list/',views.CourseListView.as_view(),name='ViewCourse'),
    path('addAssignment/', views.AssignmentCreate.as_view(), name='CreateAssignment'),
    path('assignment_list/',views.AssignmentListView.as_view(),name='ViewAssignment'),
    path('assignment/<int:pk>/update/', views.AssigmentUpdate.as_view(), name='UpdateAssignment'),
    path('Courseassignment/<int:pk>/update/', views.CourseAssigmentUpdate.as_view(), name='UpdateCourseAssignment'),
    path('assignment/<int:pk>/delete/', views.AssignmentDelete.as_view(), name='DeleteAssignment'),
    path('Courseassignment/<int:pk>/delete/', views.CourseAssignmentDelete.as_view(), name='DeleteCourseAssignment'),
    path('assignment/<int:pk>/', views.AssignmentDetailView.as_view(), name='assignment_detail'),
    path('<int:pk>/createQuestion/', views.QuestionCreate, name='CreateQuestion'),
    path('<int:assignment_pk>/UpdateQuestion/<int:question_pk>', views.QuestionUpdate, name='UpdateQuestion'),
    path('<int:assignment_pk>/DeleteQuestion/<int:pk>/delete', views.QuestionDeleteView.as_view(), name='DeleteQuestion'),
]


#STudent dashboard
urlpatterns += [
    path('StudentDashboard',views.StudentDashboard,name='StudentDashboard'),
    path('student_course_list/',views.StudentCourseListView.as_view(),name='AllCourse'),
    path('student_assigment_list/',views.StudentAssignmentListView.as_view(),name='AllAssignment'),
    path('student_course/<int:pk>', views.StudentCourseDetailView.as_view(), name='student_course_detail'),
    path('student_assignment/<int:pk>/', views.StudentAssignmentDetailView.as_view(), name='student_assignment_detail'),
    path('<int:pk>/createAnswer/', views.AnswerCreate, name='CreateAnswer'),
]
