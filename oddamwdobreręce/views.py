from django.shortcuts import render

# Create your views here.


def landingpage(request):
    return render(request, 'index.html')


def addddonation(request):
    return render(request, 'form.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')
