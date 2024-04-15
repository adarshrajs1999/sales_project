from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login

from sales_app.forms import CustomerRegister, SellerRegsiter


# Create your views here.

def home(request):
    return render(request,"home.html")

def dash(request):
    return render(request,"dash.html")

def login_1(request):
    return render(request,"login.html")

def customer_register(request):
    form=CustomerRegister()
    if request.method=="POST":
        form=CustomerRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request,"customer_register.html",{'form':form})

def seller_register(request):
    form=SellerRegsiter()
    if request.method=="POST":
        form=SellerRegsiter(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request,"seller_register.html",{'form':form})

