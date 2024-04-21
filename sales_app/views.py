from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from sales_app.forms import CustomerRegister, SellerRegsiter, LoginRegister


# Create your views here.

def home(request):
    return render(request,"home.html")

def dash(request):
    return render(request,"dash.html")

def customer_register(request):
    loginform=LoginRegister()
    customerform=CustomerRegister()
    if request.method=="POST":
        loginform=LoginRegister(request.POST)
        customerform=CustomerRegister(request.POST)
        if loginform.is_valid() and customerform.is_valid():
            loginobj=loginform.save(commit=False)
# (commit=False)--> an object need to be created but should
# not be saved to the data base immediately
            loginobj.is_customer=True
            loginobj.save()
            customerobj=customerform.save(commit=False)
            customerobj.user=loginobj
            customerobj.save()
            return redirect("/")

    return render(request,"customer_register.html",{'loginform':loginform,'customerform':customerform})

def seller_register(request):
    loginform=LoginRegister()
    sellerform=SellerRegsiter()
    if request.method=="POST":
        loginform=LoginRegister(request.POST)
        sellerform=SellerRegsiter(request.POST)
        if loginform.is_valid() and sellerform.is_valid():
            loginobj=loginform.save(commit=False)
            loginobj.is_seller=True
            loginobj.save()
            sellerobj= sellerform.save(commit=False)
            sellerobj.user=loginobj
            sellerobj.save()
            return redirect("/")

    return render(request,"seller_register.html",{'loginform':loginform,'sellerform':sellerform})


def admin_dash(request):
    return render(request,"admin/admin_dash.html")

def customer_dash(request):
    return render(request,"customer/customer_dash.html")

def seller_dash(request):
    return render(request,"seller/seller_dash.html")

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect("admin_dash")
            elif user.is_customer:
                return redirect("customer_dash")
            elif user.is_seller:
                return redirect("seller_dash")

        # else:
        #     messages.info('Invalid Credentials')
    return render(request,"login.html")

























