

from django.shortcuts import render, redirect
from sales_app.models import mobileproduct
from sales_app.forms import mobile_product_form

def create_product(request):
    data=mobile_product_form()
    if request.method=="POST":
        data=mobile_product_form(request.POST,request.FILES)
        if data.is_valid():
            data.save()
            return redirect("seller_dash")
    return render(request,"seller/add_product.html",{'data':data})

def view_products(request):
    data= mobileproduct.objects.all()
    return render(request,"seller/view_products.html",{'data':data})

def product_delete(request,id):
    product=mobileproduct.objects.get(pk=id)
    product.delete()
    return redirect('view_products')

def product_update(request,id):
    obj=mobileproduct.objects.get(pk=id)
    data=mobile_product_form(instance=obj)
    if request.method=="POST":
        data=mobile_product_form(request.POST,request.FILES,instance=obj)
        if data.is_valid():
            data.save()
            return redirect('view_products')
    return render(request,"seller/product_update.html",{"data":data})












