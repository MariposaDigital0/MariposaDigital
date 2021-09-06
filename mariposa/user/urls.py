from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('dev_signup/', views.devSignup, name='devsignup'),
    path('login/', views.login, name='login'),
    path('logout/<int:id>/', views.logout, name='logout')
]
