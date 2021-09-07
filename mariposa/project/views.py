from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from .models import Project, ProjectManager


def validate_user_session(id, token):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False


def projects(request, id, token, pid=0):
    if not validate_user_session(id, token):
        return render(request, 'notfound.html')
    UserModel = get_user_model()
    user = UserModel.objects.get(id=id)
    t_header = ['SL.No', 'Name', 'Estimated Hours',
                'Estimated Budget', 'Status', 'Progress']
    pg_data = []
    if user.u_type == 'DV':
        if request.method == 'POST':
            p = Project.objects.get(id=pid)
            p.accepted = True
            p.save()
            return redirect('/cldash/{}/{}/'.format(id, token))
        pg_data = Project.objects.filter(accepted=False).values()
        title = "New Projects"
        val = "pg"
        context = {
            'title': title,
            'val': val,
            'pg_data': pg_data,
            't_header': t_header
        }
        return render(request, 'general.html', context)
    elif user.u_type == 'CL':
        pm = ProjectManager.objects.filter(user_account_id=user).values()
        for i in pm:
            p = Project.objects.get(id=i['project_id_id'])
            pg_data.append(p)
            # print(pg_data)
            # print(i['project_id_id'])
        title = "Projects"
        val = "pg"
        context = {
            'title': title,
            'val': val,
            'pg_data': pg_data,
            't_header': t_header
        }
        return render(request, 'general.html', context)


def projectDetailView(request, id, token, pid):
    if not validate_user_session(id, token):
        return render(request, 'notfound.html')
    UserModel = get_user_model()
    user = UserModel.objects.get(id=id)
    title = "Detailed View"
    val = "pdv"
    proj = Project.objects.get(id=pid)
    context = {
        'title': title,
        'val': val,
        'proj': proj,
    }
    return render(request, 'general.html', context)


def createNewProject(request, id, token):
    user = get_user_model()
    title = 'New Project'
    val = 'np'
    if not validate_user_session(id, token):
        return render(request, 'notfound.html')
    if request.method == 'POST':
        p_name = request.POST['p_name']
        desc = request.POST['desc']
        ps_date = request.POST['p_s_d']
        pe_date = request.POST['p_e_d']
        es_hours = request.POST['esh']
        es_budget = request.POST['esb']
        p = Project(p_name=p_name, description=desc, planned_start_date=ps_date,
                    planned_end_date=pe_date, estimated_hours=es_hours, estimated_budget=es_budget)
        p.save()
        u_id = user.objects.get(id=id)
        pm = ProjectManager(project_id=p, user_account_id=u_id)
        pm.save()
        return redirect('/projects/{}/{}'.format(id, token))
    context = {
        'title': title,
        'val': val,
    }
    return render(request, 'general.html', context)
