
from django.shortcuts import render, redirect
from sales_app.models import mobileproduct, Seller, Pay, Cart
from sales_app.forms import mobile_product_form

def create_product(request):
    current_user = request.user
    seller_object = Seller.objects.get(user = current_user)
    data = mobile_product_form()
    if request.method ==  "POST":
        data = mobile_product_form(request.POST, request.FILES)
        if data.is_valid():
            product = data.save(commit = False)
            product.seller = seller_object
            product.save()
            return redirect("seller_dash")
    return render(request, "seller/add_product.html", {'data':data})

def seller_view_products(request):
    mobileproduct_objects = mobileproduct.objects.filter(seller__user = request.user)
    if request.method == "GET":
        # Giving default value as empty('')
        query = request.GET.get('query', '')
        mobileproduct_objects = mobileproduct.objects.filter(seller__user = request.user, name__icontains = query) | mobileproduct.objects.filter(seller__user = request.user, brand__icontains = query)
    return render(request,"seller/view_products.html",{'mobileproduct_objects':mobileproduct_objects})

def product_delete(request, id):
    product = mobileproduct.objects.get(pk = id)
    product.delete()
    return redirect('seller_view_products')

def product_update(request, id):
    obj =  mobileproduct.objects.get(pk = id)
    data = mobile_product_form(instance = obj)
    if request.method == "POST":
        data = mobile_product_form(request.POST, request.FILES, instance = obj)
        if data.is_valid():
            data.save()
            return redirect('seller_view_products')
    return render(request, "seller/product_update.html", {"data":data})


def view_paid_cart(request):
    pay_objects = Pay.objects.filter(buy__cart__status = 1, buy__cart__product__seller__user = request.user )
    return render(request,"seller/view_paid_cart.html",{'pay_objects':pay_objects})









