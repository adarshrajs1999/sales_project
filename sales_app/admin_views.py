from django.shortcuts import render, redirect

from sales_app.forms import CustomerRegister, SellerRegister
from sales_app.models import Customer, Seller, mobileproduct


def customer_details(request):
    customers=Customer.objects.all()
    return render(request,"admin/customer_details.html",{'customers':customers})

def seller_details(request):
    sellers=Seller.objects.all()
    return render(request, "admin/seller_details.html",{'sellers':sellers})

def customer_update(request,id):
    customer=Customer.objects.get(pk=id)
    customer_form=CustomerRegister(instance=customer)
    if request.method=="POST":
        customer_form=CustomerRegister(request.POST,instance=customer)
        if customer_form.is_valid():
            customer_form.save()
            return redirect("customer_details")
    return render(request,"admin/customer_update.html",{'customer_form':customer_form})

def seller_update(request,id):
    seller=Seller.objects.get(pk=id)
    seller_form=SellerRegister(instance=seller)
    if request.method == "POST":
        seller_form = SellerRegister(request.POST, instance=seller)
        if seller_form.is_valid():
            seller_form.save()
            return redirect("seller_details")
    return render(request,"admin/seller_update.html",{'seller_form':seller_form})

def customer_delete(request,id):
    customer=Customer.objects.get(pk=id)
    customer.delete()
    return redirect("customer_details")

def seller_delete(request,id):
    seller=Seller.objects.get(pk=id)
    seller.delete()
    return redirect("seller_details")

def admin_view_products(request):
    data= mobileproduct.objects.all()
    return render(request,"admin/view_products.html",{'data':data})

