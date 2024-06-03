from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from sales_app.filters import product_filter_form, pay_filter_form
from sales_app.forms import CustomerRegister, SellerRegister, customer_feedback_form
from sales_app.models import Customer, Seller, Product, Feedback, User_model, Pay

@login_required(login_url = 'login_view')
def customer_details(request):
    customers=Customer.objects.all()
    return render(request, "admin/customer_details.html", {'customers':customers})

@login_required(login_url = 'login_view')
def seller_details(request):
    sellers=Seller.objects.all()
    return render(request, "admin/seller_details.html", {'sellers':sellers})

@login_required(login_url = 'login_view')
def customer_update(request, id):
    customer = Customer.objects.get(pk=id)
    customer_form = CustomerRegister(instance=customer)
    if request.method == "POST":
        customer_form = CustomerRegister(request.POST,instance = customer)
        if customer_form.is_valid():
            customer_form.save()
            return redirect("customer_details")
    return render(request, "admin/customer_update.html", {'customer_form':customer_form})

@login_required(login_url = 'login_view')
def seller_update(request, id):
    seller = Seller.objects.get(pk = id)
    seller_form = SellerRegister(instance = seller)
    if request.method == "POST":
        seller_form = SellerRegister(request.POST, instance = seller)
        if seller_form.is_valid():
            seller_form.save()
            return redirect("seller_details")
    return render(request, "admin/seller_update.html", {'seller_form':seller_form})

@login_required(login_url = 'login_view')
def customer_delete(request, id):
    customer_object = Customer.objects.get(pk = id)
    user_model_object = customer_object.user
    customer_object.delete()
    user_model_object.delete()
    return redirect("customer_details")

@login_required(login_url = 'login_view')
def seller_delete(request, id):
    seller_object = Seller.objects.get(pk = id)
    user_model_object = seller_object.user
    user_model_object.delete()
    seller_object.delete()
    return redirect("seller_details")

@login_required(login_url = 'login_view')
def admin_view_products(request):
    data = Product.objects.all()
    searched_form = product_filter_form(request.GET,queryset = data)
    # qs-->query set
    data = searched_form.qs
    context = {'data': data, 'searched_form': searched_form}
    return render(request, "admin/view_products.html", context)

@login_required(login_url = 'login_view')
def admin_view_feedbacks(request):
    feedback_objects = Feedback.objects.all()
    return render(request, "admin/view_feedbacks.html",{'feedback_objects':feedback_objects})

@login_required(login_url = 'login_view')
def admin_view_orders(request):
    pay_objects = Pay.objects.all()
    pay_filter_form_data = pay_filter_form(request.GET, queryset=pay_objects)
    pay_objects = pay_filter_form_data.qs
    context = {'pay_objects':pay_objects, 'pay_filter_form_data':pay_filter_form_data}
    return render(request, "admin/admin_view_orders.html", context)

@login_required(login_url = 'login_view')
def admin_update_reply(request, feedback_object_id):
    feedback_object = Feedback.objects.get(id = feedback_object_id)
    if request.method == 'POST':
        reply = request.POST.get('reply')
        feedback_object.reply = reply
        feedback_object.save()
        return redirect('admin_view_feed_backs')
    return render(request, "admin/admin_update_reply.html", {'feedback_object':feedback_object})