from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from mariposa.project.models import Project, ProjectManager


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
    UserModel = get_user_model()
    user = UserModel.objects.get(id=id)
    pm = ProjectManager.objects.filter(user_account_id=user).values()
    pg_data = []
    for i in pm:
        p = Project.objects.get(id=i['project_id_id'])
        pg_data.append(p)
        # print(pg_data)
        # print(i['project_id_id'])
    title = "Client Dashboard"
    val = "cdb"
    context = {
        'title': title,
        'val': val,
        'pg_data': pg_data,
    }
    return render(request, 'general.html', context)
