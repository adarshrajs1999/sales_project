from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from sales_app.forms import pay_form, customer_feedback_form, CustomerRegister
from sales_app.models import Product, Customer, Cart, Buy, Pay, Feedback
from sales_app.filters import  product_filter_form

@login_required(login_url = 'login_view')
def customer_view_products(request):
    product_objects = Product.objects.all()
    searched_form = product_filter_form(request.GET,queryset = product_objects)
    # qs-->query set
    product_objects = searched_form.qs

    paginator = Paginator(product_objects, 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    customer_object = Customer.objects.get(user=request.user)
    context = {'page_obj': page_obj,'searched_form':searched_form, 'customer_object': customer_object}
    return render(request, "customer/view_products.html", context)

@login_required(login_url = 'login_view')
def add_to_cart(request,product_id):
        customer_object = Customer.objects.get(user = request.user)
        product_object = Product.objects.get(pk = product_id)
        cart_obj = Cart(customer = customer_object, product = product_object)
        cart_obj.save()
        return redirect('customer_view_products')


# get()-->Used when you expect to retrieve exactly one object.
# filter()-->Used when you expect to retrieve zero or more objects.

@login_required(login_url = 'login_view')
def view_cart(request):
    customer_object = Customer.objects.get(user = request.user)
    cart_objects = Cart.objects.filter(customer = customer_object)
    customer_object = Customer.objects.get(user=request.user)
    return render(request, "customer/view_cart.html",{'cart_objects':cart_objects,  'customer_object': customer_object})

@login_required(login_url = 'login_view')
def delete_cart(request, id):
    cart_object = Cart.objects.get(pk = id)
    cart_object.delete()
    return redirect("view_cart")

@login_required(login_url = 'login_view')
def buy(request, cart_id):
    cart_object = Cart.objects.get(id=cart_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 0))
        adress = request.POST.get('adress')
        phone = request.POST.get('phone')
        price = int(cart_object.product.price)
        amount = quantity*price
        if cart_object.buy_status == 0:
            buy_object = Buy(cart = cart_object,quantity = quantity,adress = adress,
            phone = phone,amount = amount)
            buy_object.save()
            cart_object.buy_status = 1
            cart_object.save()
        elif cart_object.buy_status == 1:
            buy_object = Buy.objects.get(cart = cart_object)
            buy_object.quantity = quantity
            buy_object.adress =adress
            buy_object.phone = phone
            buy_object.amount = amount
            buy_object.save()
        return redirect("pay", buy_object_id = buy_object.id)
    customer_object = Customer.objects.get(user = request.user)
    return render(request, "customer/buy.html",{'customer_object': customer_object})


@login_required(login_url = 'login_view')
def pay(request, buy_object_id):
    buy_object = Buy.objects.get(id=buy_object_id)
    pay_form_object = pay_form()
    if request.method == 'POST':
        pay_form_object = pay_form(request.POST)
        if pay_form_object.is_valid():
            pay_object = pay_form_object.save(commit = False)
            pay_object.buy = buy_object
            pay_object.save()
            buy_object.pay_status = 1
            buy_object.save()
            return redirect('view_cart')
    customer_object = Customer.objects.get(user=request.user)
    return render(request, 'customer/payment.html', {'data':pay_form_object, 'buy_object':buy_object, 'customer_object': customer_object})

@login_required(login_url = 'login_view')
def view_my_orders(request):
    pay_objects = Pay.objects.filter(buy__cart__customer__user = request.user)
    customer_object = Customer.objects.get(user = request.user)
    return render(request, 'customer/view_my_orders.html', {'pay_objects': pay_objects,  'customer_object': customer_object})

@login_required(login_url = 'login_view')
def customer_feed_back(request):
    feedback_form_data = customer_feedback_form()
    if request.method == 'POST':
        feedback_form_data = customer_feedback_form(request.POST)
        if feedback_form_data.is_valid():
            feedback_object = feedback_form_data.save(commit = False)
            feedback_object.customer = Customer.objects.get(user = request.user)
            feedback_object.save()
            return redirect('customer_dash')
    customer_object = Customer.objects.get(user=request.user)
    return render(request, "customer/customer_feed_back.html",{'feedback_form_data':feedback_form_data, 'customer_object': customer_object})

@login_required(login_url = 'login_view')
def customer_view_feedbacks(request):
    feedback_objects = Feedback.objects.filter(customer__user = request.user).order_by('-date')
    customer_object = Customer.objects.get(user=request.user)
    return render(request, "customer/view_feedbacks.html",{'feedback_objects':feedback_objects, 'customer_object': customer_object})

@login_required(login_url = 'login_view')
def customer_delete_feedback(request, feedback_object_id):
    feedback_object = Feedback.objects.get(id = feedback_object_id)
    feedback_object.delete()
    return redirect('customer_view_feed_backs')


def customer_profile_update(request):
    customer_object = Customer.objects.get(user = request.user)
    customer_form_object = CustomerRegister(instance = customer_object)
    if request.method == 'POST':
        customer_form_object = CustomerRegister(request.POST,request.FILES, instance = customer_object)
        if customer_form_object.is_valid():
            customer_form_object.save()
            return redirect('customer_profile_update')
    customer_object = Customer.objects.get(user=request.user)
    return render(request,"customer/customer_profile_update.html",{'customer_form_object':customer_form_object,'customer_object':customer_object})






