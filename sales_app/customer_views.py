from django.shortcuts import render, redirect
from sales_app.models import mobileproduct, Customer, Cart
from sales_app.filters import  product_filter_form

def customer_view_products(request):
    data = mobileproduct.objects.all()
    searched_form = product_filter_form(request.GET,queryset=data)
    # qs-->query set
    data =searched_form.qs
    context={'data':data,'searched_form':searched_form}
    return render(request,"customer/view_products.html",context)

def add_to_cart(request,id):
        customer_object=Customer.objects.get(user=request.user)
        product_object=mobileproduct.objects.get(pk=id)
        cart_obj=Cart(customer=customer_object, product=product_object)
        cart_obj.save()
        return redirect('customer_view_products')


# get-->Used when you expect to retrieve exactly one object.
# filter()-->Used when you expect to retrieve zero or more objects.

def view_cart(request):
    customer_object=Customer.objects.get(user=request.user)
    cart_objects=Cart.objects.filter(customer=customer_object)
    data=cart_objects
    return render(request,"customer/view_cart.html",{'data':data})


def delete_cart(request,id):
    cart_object=Cart.objects.get(pk=id)
    cart_object.delete()
    return redirect("view_cart")









