from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login

from sales_app.forms import CustomerRegister, SellerRegsiter, LoginRegister


# Create your views here.

def home(request):
    return render(request,"home.html")

def dash(request):
    return render(request,"dash.html")

def login_1(request):
    return render(request,"login.html")


def customer_register(request):
    formlogin=LoginRegister()
    formcustomer=CustomerRegister()
    if request.method=="POST":
        formlogin=LoginRegister(request.POST)
        formcustomer=CustomerRegister(request.POST)
        if formlogin.is_valid() and formcustomer.is_valid():
            loginobj=formlogin.save(commit=False)
            loginobj.is_customer=True
            loginobj.save()
            customerobj=formcustomer.save(commit=False)
            customerobj.user=loginobj
            customerobj.save()
            return redirect("/")

    return render(request,"customer_register.html",{'formlogin':formlogin,'formcustomer':formcustomer})

def seller_register(request):
    formlogin=LoginRegister()
    formseller=SellerRegsiter()
    if request.method=="POST":
        formlogin=LoginRegister(request.POST)
        formseller=SellerRegsiter(request.POST)
        if formlogin.is_valid() and formseller.is_valid():
            loginobj=formlogin.save(commit=False)
            loginobj.is_seller=True
            loginobj.save()
            sellerobj= formseller.save(commit=False)
            sellerobj.user=loginobj
            sellerobj.save()
            return redirect("/")

    return render(request,"seller_register.html",{'formlogin':formlogin,'formseller':formseller})

























