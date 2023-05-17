from django.shortcuts import render
from .models import Donation, Institution
from django.db.models import Sum

# Create your views here.


def landingpage(request):
    quantity = Donation.objects.aggregate(TOTAL=Sum('quantity'))['TOTAL']
    institution = Institution.objects.aggregate(TOTAL=Sum('name'))['TOTAL']
    return render(request, 'index.html', {'quantity': quantity, 'institution': institution})


def addddonation(request):
    return render(request, 'form.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')
