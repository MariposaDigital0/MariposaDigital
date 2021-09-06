from django.shortcuts import render, redirect
from .models import Contact


def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['text']
        con = Contact(name=name, email=email, descrip=text)
        con.save()
        return redirect('/')
    else:
        title = "Mariposa Home"
        login = "login"
        signup = "signup"
        tp = "CL"
        context = {
            'login': login,
            'signup': signup,
            'title': title,
            'tp': tp,
        }
        return render(request, 'home.html', context)


def devHome(request):
    title = "Mariposa Developers"
    login = "login"
    signup = "dev_signup"
    context = {
        'login': login,
        'signup': signup,
        'title': title,
    }
    return render(request, 'dev.html', context)
