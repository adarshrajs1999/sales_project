from django.shortcuts import render, redirect

from sales_app.forms import pay_form, customer_feedback_form
from sales_app.models import mobileproduct, Customer, Cart, Buy, Pay, Feedback
from sales_app.filters import  product_filter_form

def customer_view_products(request):
    data = mobileproduct.objects.all()
    searched_form = product_filter_form(request.GET,queryset = data)
    # qs-->query set
    data = searched_form.qs
    customer_object = Customer.objects.get(user=request.user)
    context = {'data':data,'searched_form':searched_form, 'customer_object': customer_object}
    return render(request, "customer/view_products.html", context)

def add_to_cart(request,product_id):
        customer_object = Customer.objects.get(user = request.user)
        product_object = mobileproduct.objects.get(pk = product_id)
        cart_obj = Cart(customer = customer_object, product = product_object)
        cart_obj.save()
        return redirect('customer_view_products')


# get()-->Used when you expect to retrieve exactly one object.
# filter()-->Used when you expect to retrieve zero or more objects.

def view_cart(request):
    customer_object = Customer.objects.get(user = request.user)
    cart_objects = Cart.objects.filter(customer = customer_object)
    customer_object = Customer.objects.get(user=request.user)
    return render(request, "customer/view_cart.html",{'cart_objects':cart_objects,  'customer_object': customer_object})


def delete_cart(request, id):
    cart_object = Cart.objects.get(pk = id)
    cart_object.delete()
    return redirect("view_cart")

def buy(request, cart_id):
    if request.method == 'POST':
        cart_object = Cart.objects.get(id = cart_id)
        cart = cart_object
        quantity = int(request.POST.get('quantity', 0))
        adress = request.POST.get('adress')
        phone = request.POST.get('phone')
        price = int(cart_object.product.price)
        amount = quantity*price
        buy_object = Buy(cart = cart,quantity = quantity,adress = adress,
        phone = phone,amount = amount)
        buy_object.save()
        current_obect_id = buy_object.id
        return redirect("pay", buy_id = current_obect_id)
    customer_object = Customer.objects.get(user = request.user)
    return render(request, "customer/buy.html",{'customer_object': customer_object})


def pay(request, buy_id):
    data = pay_form()
    buy_object = Buy.objects.get(id = buy_id)
    if request.method == 'POST':
        data = pay_form(request.POST)
        if data.is_valid():
            pay_object = data.save(commit = False)
            pay_object.buy = buy_object
            pay_object.save()
            cart_object =buy_object.cart
            cart_object.status = 1
            cart_object.save()
            return redirect('view_cart')
    customer_object = Customer.objects.get(user=request.user)
    return render(request, 'customer/payment.html', {'data':data, 'buy_object':buy_object, 'customer_object': customer_object})

def view_my_orders(request):
    pay_objects = Pay.objects.filter(buy__cart__customer__user = request.user)
    customer_object = Customer.objects.get(user=request.user)
    return render(request, 'customer/view_my_orders.html', {'pay_objects': pay_objects,  'customer_object': customer_object})

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

def customer_view_feedbacks(request):
    feedback_objects = Feedback.objects.filter(customer__user = request.user)
    customer_object = Customer.objects.get(user=request.user)
    return render(request, "customer/view_feedbacks.html",{'feedback_objects':feedback_objects, 'customer_object': customer_object})

def customer_delete_feedback(request, feedback_object_id):
    feedback_object = Feedback.objects.get(id = feedback_object_id)
    feedback_object.delete()
    return redirect('customer_view_feed_backs')






