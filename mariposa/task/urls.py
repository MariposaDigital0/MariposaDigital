from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name="tasks"),
    path('<int:tid>/', views.tasks, name="tasks"),
    path('newtask/', views.CreateNewTask, name="newtask"),
    path('task_detail_view/<int:tid>',
         views.taskDetailView, name="td_view"),
    path('edit_task/<int:tid>',
         views.taskEdit, name="ed_task"),
]
