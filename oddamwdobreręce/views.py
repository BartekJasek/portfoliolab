from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import Donation, Institution, Category, User

# Create your views here.


class LandingPage(View):
    def get(self, request, *args, **kwargs):
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
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        fundations = Institution.objects.all()
        return render(request, 'form.html', {'categories': categories, 'fundations': fundations})


class Login(View):
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/register')
        return render(request, 'login.html')


class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')


class Register(View):
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('name')
        last_name = request.POST.get('surname')
        user = User.objects.create(email=email, password=password, first_name=first_name, last_name=last_name)
        return redirect('/login')
        return render(request, 'register.html')
