from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('agreement/', views.agreement, name="agreement"),
    path('payment/', views.payment, name="payment")
]
