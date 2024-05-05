from django.shortcuts import render
from sales_app.models import mobileproduct
from sales_app.filters import  product_filter_form

def customer_view_products(request):
    data = mobileproduct.objects.all()
    searched_form = product_filter_form(request.GET,queryset=data)
    # qs-->query set
    data =searched_form.qs
    context={'data':data,'searched_form':searched_form}
    return render(request,"customer/view_products.html",context)

