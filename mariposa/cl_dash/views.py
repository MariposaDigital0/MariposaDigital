from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from .models import Requirments, Jobs
from .forms import UploadFileForm


def validate_user_session(id, token):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False


def dashboard(request, id, token):
    if not validate_user_session(id, token):
        return render(request, 'notfound.html')
    context = {
    }
    return render(request, 'general.html', context)


def CreateNewProject(request, id, token):
    title = 'New Project'
    val = 'np'
    if not validate_user_session(id, token):
        return render(request, 'notfound.html')
    context = {
        'title': title,
        'val': val,
    }
    return render(request, 'general.html', context)


def agreement(request, id, token):
    User = get_user_model()
    user = User.objects.get(id=id)
    if not validate_user_session(id, token):
        return render(request, 'notfound.html')
    else:
        context = {

        }
        return render(request, 'agreement.html', context)


def payment(request, id, token):
    User = get_user_model()
    user = User.objects.get(id=id)
    if not validate_user_session(id, token):
        return render(request, 'notfound.html')
    else:
        context = {

        }
        return render(request, 'payment.html', context)
