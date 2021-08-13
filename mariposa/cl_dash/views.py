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
    User = get_user_model()
    user = User.objects.get(id=id)
    jobs = Jobs.objects.filter(user_id=user.id).values()
    if not validate_user_session(id, token):
        return render(request, 'notfound.html')
    if request.POST:
        form = UploadFileForm(request.FILES)
        if form.is_valid():
            print("Valid")
            instance = Requirments(
                req=request.FILES['file'], user_id=user.id)
            instance.save()
        print("Not valid")
        return redirect('/dashboard/{}/{}/'.format(user.id, user.session_token))
    else:
        form = UploadFileForm()
        context = {
            'jobs': jobs,
            'form': form,
        }
        return render(request, 'dashboard.html', context)


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
