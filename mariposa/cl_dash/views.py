from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model


def validate_user_session(id, token):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False


def cldash(request, id, token):
    if not validate_user_session(id, token):
        return render(request, 'notfound.html')
    title = "Client Dashboard"
    val = "cdb"
    context = {
        'title': title,
        'val': val,
    }
    return render(request, 'general.html', context)
