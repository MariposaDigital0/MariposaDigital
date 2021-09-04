from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from mariposa.project.models import Project, ProjectManager
from .models import Task


def validate_user_session(id, token):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False


def CreateNewTask(request, id, token):
    if not validate_user_session(id, token):
        return render(request, 'notfound.html')
    title = "Create Tasks"
    val = "ctk"
    UserModel = get_user_model()
    user = UserModel.objects.get(id=id)
    pm = ProjectManager.objects.filter(user_account_id=user).values()
    t_data = []
    for i in pm:
        p = Project.objects.get(id=i['project_id_id'])
        t_data.append(p)
        print(t_data)
        # print(i['project_id_id'])
    if request.method == 'POST':
        project = request.POST['project']
        name = request.POST['t_name']
        desc = request.POST['desc']
        prio = request.POST['prio']
        ps_date = request.POST['p_s_d']
        pe_date = request.POST['p_e_d']
        es_hours = request.POST['esh']
        es_budget = request.POST['esb']
        p = Project.objects.get(id=project)
        t = Task(project_id=p, t_name=name, description=desc, priority=prio, planned_start_date=ps_date,
                 planned_end_date=pe_date, estimated_hours=es_hours, estimated_budget=es_budget)
        t.save()
        return redirect('/tasks/{}/{}'.format(id, token))
    context = {
        'title': title,
        'val': val,
        't_data': t_data
    }
    return render(request, 'general.html', context)


def tasks(request, id, token):
    if not validate_user_session(id, token):
        return render(request, 'notfound.html')
    title = "Tasks"
    val = "tk"
    UserModel = get_user_model()
    user = UserModel.objects.get(id=id)
    t_header = ['SL.No', 'Name', 'Estimated Hours',
                'Estimated Budget', 'Priority']
    pm = ProjectManager.objects.filter(user_account_id=user).values()
    t_data = []
    for i in pm:
        p = Project.objects.get(id=i['project_id_id'])
        tx = Task.objects.filter(project_id=p).values()
        for j in tx:
            t_data.append(j)
            # print(t_data)
            # print(i['project_id_id'])
    context = {
        'title': title,
        'val': val,
        't_header': t_header,
        't_data': t_data,
    }
    return render(request, 'general.html', context)
