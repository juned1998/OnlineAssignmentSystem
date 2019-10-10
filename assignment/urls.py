from django.urls import path
from . import views

urlpatterns = [
    #path('',views.index,name='home')
    path('',views.QuestionListView.as_view(),name='index'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('question/<int:pk>', views.QuestionDetailView.as_view(), name='question-detail'),
]

urlpatterns += [
    path('course/all',views.CourseListView.as_view(),name="course-list"),
    path('course/create/', views.CourseCreate.as_view(), name='course_create'),
    path('course/<int:pk>/update/', views.CourseUpdate.as_view(), name='course_update'),
    path('course/<int:pk>/delete/', views.CourseDelete.as_view(), name='course_delete'),
    path('course/<int:pk>',views.CourseDetailView.as_view() ,name = 'course-detail' )
]



urlpatterns += [
    path('emp', views.emp),
    path('show',views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
]
