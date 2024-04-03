from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login

# Create your views here.

def home(request):
    return render(request,"home.html")

def dash(request):
    return render(request,"dash.html")

def login_1(request):
    return render(request,"login.html")


