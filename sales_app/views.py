from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from sales_app.forms import CustomerRegister, User_form, SellerRegister
from sales_app.models import Customer, Seller


# Create your views here.

@login_required(login_url = 'login_view')
def home(request):
    return render(request, "home.html")

@login_required(login_url = 'login_view')
def dash(request):
    return render(request, "dash.html")


def customer_register(request):
    user_form = User_form()
    customerform = CustomerRegister()
    if request.method == "POST":
        user_form = User_form(request.POST)
        customerform = CustomerRegister(request.POST, request.FILES)
        if user_form.is_valid() and customerform.is_valid():
            user_obj = user_form.save(commit = False)
# (commit = False)--> an object need to be created but should
# not be saved to the data base immediately
            user_obj.is_customer = True
            user_obj.save()
            customer_obj = customerform.save(commit = False)
            customer_obj.user = user_obj
            customer_obj.save()
            return redirect("/")

    return render(request,"customer_register.html", {'user_form':user_form, 'customer_form':customerform})


def seller_register(request):
    user_form = User_form()
    sellerform = SellerRegister()
    if request.method == "POST":
        user_form = User_form(request.POST)
        sellerform = SellerRegister(request.POST, request.FILES)
        if user_form.is_valid() and sellerform.is_valid():
            user_obj = user_form.save(commit = False)
            user_obj.is_seller = True
            user_obj.save()
            seller_obj = sellerform.save(commit = False)
            seller_obj.user = user_obj
            seller_obj.save()
            return redirect("/")

    return render(request,"seller_register.html", {'user_form':user_form, 'sellerform':sellerform})

@login_required(login_url = 'login_view')
def admin_dash(request):
    return render(request,"admin/admin_dash.html")

@login_required(login_url = 'login_view')
def customer_dash(request):
    customer_object = Customer.objects.get(user = request.user)
    return render(request,"customer/customer_dash.html", {'customer_object':customer_object})

@login_required(login_url = 'login_view')
def seller_dash(request):
    seller_object = Seller.objects.get(user = request.user)
    return render(request,"seller/seller_dash.html", {'seller_object':seller_object})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_object = authenticate(request, username = username, password = password)
        if user_object is not None:
            login(request , user_object)
            if user_object.is_staff:
                return redirect("admin_dash")
            elif user_object.is_customer:
                return redirect("customer_dash")
            elif user_object.is_seller:
                return redirect("seller_dash")
        else:
            messages.info(request, 'Invalid Credentials')
    return render(request, "login.html")

@login_required(login_url = 'login_view')
def logout_view(request):
    logout(request)
    return redirect('login_view')























