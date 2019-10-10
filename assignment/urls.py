from django.urls import path
from . import views

urlpatterns = [
    #path('',views.index,name='home')
    path('',views.QuestionListView.as_view(),name='index'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('question/<int:pk>', views.QuestionDetailView.as_view(), name='question-detail'),
]
