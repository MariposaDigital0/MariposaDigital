from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('user/', include('mariposa.user.urls')),
    path('dashboard/<int:id>/<str:token>/', include('mariposa.cl_dash.urls')),
    path('projects/<int:id>/<str:token>/', include('mariposa.project.urls')),
    path('tasks/<int:id>/<str:token>/', include('mariposa.task.urls')),
]
