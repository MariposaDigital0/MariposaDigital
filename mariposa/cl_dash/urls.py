from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('createnew/', views.CreateNewProject, name="newproject"),
    path('agreement/', views.agreement, name="agreement"),
    path('payment/', views.payment, name="payment")
]
