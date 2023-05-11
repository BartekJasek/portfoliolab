from django.shortcuts import render
import sqlite3

# Create your views here.


def landingpage(request):
    databaseconnect = sqlite3.connect('charity-donation')
    cursor1 = databaseconnect.cursor()
    cursor2 = databaseconnect.cursor()
    bag = "SELECT TOTAL(quantity) FROM oddamwdobreręce_donation"
    fund = "SELECT count(*) FROM oddamwdobreręce_institution"
    cursor1.execute(bag)
    cursor2.execute(fund)
    bag = cursor1.fetchall()
    fund = cursor2.fetchall()
    databaseconnect.close()
    return render(request, 'index.html', {'bag': bag, 'fund': fund})


def addddonation(request):
    return render(request, 'form.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')
