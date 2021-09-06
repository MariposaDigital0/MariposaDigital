from django.contrib.auth import models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import get_user_model
import random

User = get_user_model()


def generate_session_token(length=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97, 123)]+[str(i) for i in range(10)]) for _ in range(length))


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['f_name']
        last_name = request.POST['l_name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['ph_no']
        password = request.POST['password']
        conf_pass = request.POST['conf_pass']
        if password == conf_pass:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('/')
            else:
                user = User.objects.create_user(
                    username=username, password=password, email=email, phone=phone, first_name=first_name, last_name=last_name, u_type='CL')
                user.save()
                print(request, 'user created')
                return redirect('/')
        else:
            messages.info(request, 'password not matching')
            return redirect('/')
    else:
        context = {
        }
        return render(request, 'signup.html', context)


def devSignup(request):
    if request.method == 'POST':
        first_name = request.POST['f_name']
        last_name = request.POST['l_name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['ph_no']
        password = request.POST['password']
        conf_pass = request.POST['conf_pass']
        if password == conf_pass:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('/')
            else:
                user = User.objects.create_user(
                    username=username, password=password, email=email, phone=phone, first_name=first_name, last_name=last_name, u_type='DV')
                user.save()
                print(request, 'user created')
                return redirect('/')
        else:
            messages.info(request, 'password not matching')
            return redirect('/')
    else:
        context = {
        }
        return render(request, 'signup.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            token = generate_session_token()
            user.session_token = token
            user.save()
            auth.login(request, user)
            if user.u_type == 'CL':
                return redirect('/cldash/{}/{}/'.format(user.id, user.session_token))
            elif user.u_type == 'DV':
                pass
            else:
                pass
        else:
            messages.info(request, 'Wrong email or password')
            return redirect("/")
    else:
        return redirect('/')


def logout(request, id):
    user = User.objects.get(pk=id)
    user.session_token = "0"
    user.save()
    auth.logout(request)
    return redirect('/')
