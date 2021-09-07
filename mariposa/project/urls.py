from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name="projects"),
    path('<int:pid>/', views.projects, name="projects"),
    path('createnew/', views.createNewProject, name="newproject"),
    path('project_detail_view/<int:pid>',
         views.projectDetailView, name="pd_view"),
]
