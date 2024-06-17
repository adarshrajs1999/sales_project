from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from sales_app.models import Product, Seller, Pay, Cart, Customer
from sales_app.forms import mobile_product_form

@login_required(login_url = 'login_view')
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
    seller_object = Seller.objects.get(user = request.user)
    return render(request, "seller/add_product.html", {'data':data, 'seller_object':seller_object})

@login_required(login_url = 'login_view')
def seller_view_products(request):
    mobileproduct_objects = Product.objects.filter(seller__user = request.user)
    if request.method == "GET":
        # Giving default value as empty('')
        query = request.GET.get('query', '')
        mobileproduct_objects = Product.objects.filter(seller__user = request.user, name__icontains = query) | Product.objects.filter(seller__user = request.user, brand__icontains = query)
    seller_object = Seller.objects.get(user=request.user)
    return render(request,"seller/view_products.html",{'mobileproduct_objects':mobileproduct_objects, 'seller_object':seller_object})

@login_required(login_url = 'login_view')
def product_delete(request, id):
    product_object = Product.objects.get(pk = id)
    product_object.delete()
    return redirect('seller_view_products')

@login_required(login_url = 'login_view')
def product_update(request, id):
    obj =  Product.objects.get(pk = id)
    data = mobile_product_form(instance = obj)
    if request.method == "POST":
        data = mobile_product_form(request.POST, request.FILES, instance = obj)
        if data.is_valid():
            data.save()
            return redirect('seller_view_products')
    seller_object = Seller.objects.get(user=request.user)
    return render(request, "seller/product_update.html", {"data":data, 'seller_object':seller_object})

@login_required(login_url = 'login_view')
def view_paid_cart(request):
    pay_objects = Pay.objects.filter(buy__cart__status = 1, buy__cart__product__seller__user = request.user )
    seller_object = Seller.objects.get(user=request.user)
    return render(request,"seller/view_paid_orders.html",{'pay_objects':pay_objects, 'seller_object':seller_object})








