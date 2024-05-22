from django.shortcuts import render, redirect

from sales_app.filters import product_filter_form
from sales_app.forms import CustomerRegister, SellerRegister
from sales_app.models import Customer, Seller, mobileproduct, Feedback


def customer_details(request):
    customers=Customer.objects.all()
    return render(request, "admin/customer_details.html", {'customers':customers})

def seller_details(request):
    sellers=Seller.objects.all()
    return render(request, "admin/seller_details.html", {'sellers':sellers})

def customer_update(request, id):
    customer = Customer.objects.get(pk=id)
    customer_form = CustomerRegister(instance=customer)
    if request.method == "POST":
        customer_form = CustomerRegister(request.POST,instance = customer)
        if customer_form.is_valid():
            customer_form.save()
            return redirect("customer_details")
    return render(request, "admin/customer_update.html", {'customer_form':customer_form})

def seller_update(request, id):
    seller = Seller.objects.get(pk = id)
    seller_form = SellerRegister(instance = seller)
    if request.method == "POST":
        seller_form = SellerRegister(request.POST, instance = seller)
        if seller_form.is_valid():
            seller_form.save()
            return redirect("seller_details")
    return render(request, "admin/seller_update.html", {'seller_form':seller_form})

def customer_delete(request, id):
    customer = Customer.objects.get(pk = id)
    customer.delete()
    return redirect("customer_details")

def seller_delete(request, id):
    seller = Seller.objects.get(pk = id)
    seller.delete()
    return redirect("seller_details")

def admin_view_products(request):
    data = mobileproduct.objects.all()
    searched_form = product_filter_form(request.GET,queryset = data)
    # qs-->query set
    data = searched_form.qs
    context = {'data': data, 'searched_form': searched_form}
    return render(request, "admin/view_products.html", context)

def admin_view_feedbacks(request):
    feedback_objects = Feedback.objects.all()
    if request.method == 'POST':
        reply = request.POST.get('reply')
        current_feedback_id = request.POST.get("current_feedback_object_id")
        current_feedback_object = Feedback.objects.get(id = current_feedback_id)
        current_feedback_object.reply = reply
        current_feedback_object.status = 1
        current_feedback_object.save()
        return redirect("admin_view_feed_backs")
    return render(request, "admin/view_feedbacks.html",{'feedback_objects':feedback_objects})