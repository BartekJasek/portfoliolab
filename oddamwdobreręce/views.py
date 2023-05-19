from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import Donation, Institution, Category
from .forms import UserCreationForm, LoginForm

# Create your views here.


class LandingPage(View):
    def get(self, request):
        quantity = Donation.objects.aggregate(TOTAL=Sum('quantity'))['TOTAL']
        institution = Institution.objects.aggregate(TOTAL=Sum('name'))['TOTAL']

        fundations = Institution.objects.filter(subject='fundacja')
        nongovermentals = Institution.objects.filter(subject='organizacja pozarządowa')
        collections = Institution.objects.filter(subject='zbiórka lokalna')

        return render(request, 'index.html', {'quantity': quantity, 'institution': institution,
                                          'nongovermentals': nongovermentals, 'fundations': fundations,
                                          'collections': collections})


#@login_required(login_url='/login')
class AddDonation(View):
    def get(self, request):
        categories = Category.objects.all()
        fundations = Institution.objects.all()
        return render(request, 'form.html', {'categories': categories, 'fundations': fundations})


class Login(View):
    def get(self, request):
        loginform = LoginForm()
        return render(request, 'login.html', {'loginform': loginform})

    def post(self, request):
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            email = loginform.cleaned_data['email']
            password = loginform.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return redirect('/register')

        return render(request, 'login.html', {'loginform': loginform})


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class Register(View):
    def get(self, request):
        registerform = UserCreationForm()
        return render(request, 'register.html', {'registerform': registerform})

    def post(self, request):
        registerform = UserCreationForm(request.POST)
        if registerform.is_valid():
            user = registerform.save()
            return redirect('/login')
