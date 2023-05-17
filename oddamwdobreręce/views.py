from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.db.models import Sum
from .models import Donation, Institution
from .forms import UserCreationForm

# Create your views here.


def landingpage(request):
    quantity = Donation.objects.aggregate(TOTAL=Sum('quantity'))['TOTAL']
    institution = Institution.objects.aggregate(TOTAL=Sum('name'))['TOTAL']

    fundations = Institution.objects.filter(subject='fundacja')
    nongovermentals = Institution.objects.filter(subject='organizacja pozarządowa')
    collections = Institution.objects.filter(subject='zbiórka lokalna')

    return render(request, 'index.html', {'quantity': quantity, 'institution': institution,
                                          'nongovermentals': nongovermentals, 'fundations': fundations,
                                          'collections': collections})


def addddonation(request):
    return render(request, 'form.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/register')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        registerform = UserCreationForm(request.POST)
        if registerform.is_valid():
            user = registerform.save()
            return redirect('/login')
    else:
        registerform = UserCreationForm()
    return render(request, 'register.html', {'registerform': registerform})
