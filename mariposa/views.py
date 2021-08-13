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
        context = {
            'title': title
        }
        return render(request, 'home.html', context)
