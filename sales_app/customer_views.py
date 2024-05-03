from django.shortcuts import render
from sales_app import filters
from sales_app.models import mobileproduct
from sales_app.filters import search_product

def customer_view_products(request):
    data= mobileproduct.objects.all()
    search_filter = search_product(request.GET, queryset=data)
    data = search_filter.qs
    return render(request,"customer/view_products.html",{'data':data,'search_filter':search_filter})

# def customer_product_search(request):
#     products=mobileproduct.objects.all()
#     search_filter=search_product(request.GET,queryset=products)
#     products=search_filter.qs
#
#     context={
#         'products':products,
#         'search_filter':search_filter
#     }
#     return render(request,'customer/view_products.html',context)
