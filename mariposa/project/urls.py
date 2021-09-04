from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name="projects"),
    path('createnew/', views.CreateNewProject, name="newproject"),
]
