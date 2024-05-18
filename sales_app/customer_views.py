from django.shortcuts import render, redirect

from sales_app.forms import pay_form
from sales_app.models import mobileproduct, Customer, Cart, Buy
from sales_app.filters import  product_filter_form

def customer_view_products(request):
    data = mobileproduct.objects.all()
    searched_form = product_filter_form(request.GET,queryset = data)
    # qs-->query set
    data = searched_form.qs
    context = {'data':data,'searched_form':searched_form}
    return render(request,"customer/view_products.html",context)

def add_to_cart(request,id):
        customer_object = Customer.objects.get(user = request.user)
        product_object = mobileproduct.objects.get(pk = id)
        cart_obj = Cart(customer = customer_object, product = product_object)
        cart_obj.save()
        return redirect('customer_view_products')


# get()-->Used when you expect to retrieve exactly one object.
# filter()-->Used when you expect to retrieve zero or more objects.

def view_cart(request):
    customer_object = Customer.objects.get(user = request.user)
    cart_objects = Cart.objects.filter(customer = customer_object)
    return render(request,"customer/view_cart.html",{'cart_objects':cart_objects})


def delete_cart(request,id):
    cart_object = Cart.objects.get(pk = id)
    cart_object.delete()
    return redirect("view_cart")

def buy(request,cart_id):
    if request.method == 'POST':
        cart_object = Cart.objects.get(id=cart_id)
        cart = cart_object
        quantity = int(request.POST.get('quantity',0))
        adress = request.POST.get('adress')
        phone = request.POST.get('phone')
        price = int(cart_object.product.price)
        amount = quantity*price
        buy_object = Buy(cart = cart,quantity = quantity,adress = adress,
        phone = phone,amount = amount)
        buy_object.save()
        current_obect_id=buy_object.id
        return redirect("pay",buy_id = current_obect_id)
    return render(request,"customer/buy.html")


def pay(request,buy_id):
    data = pay_form()
    buy_object = Buy.objects.get(id = buy_id)
    if request.method == 'POST':
        data = pay_form(request.POST)
        if data.is_valid():
            pay_object = data.save(commit = False)
            buy_obj=Buy.objects.get(id = buy_id)
            pay_object.buy = buy_obj
            pay_object.save()
            cart_object =buy_object.cart
            cart_object.status = 1
            cart_object.save()
            return redirect('view_cart')
    return render(request,'customer/payment.html',{'data':data,'buy_object':buy_object})











