from django.shortcuts import render
from sales_app import filters
from sales_app.models import mobileproduct
from sales_app.filters import  product_filter

def customer_view_products(request):
    data = mobileproduct.objects.all()
    searched_form = product_filter(request.GET,queryset=data)
    data = searched_form.qs
    return render(request,"customer/view_products.html",{'data':data,'searched_form':searched_form})

