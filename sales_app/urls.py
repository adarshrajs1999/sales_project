from django.urls import path

from sales_app import views

urlpatterns = [
    path("",views.home,name="home"),
    path("dash/",views.dash,name="dash"),
    path("login/",views.login_view,name="login_view"),
    path("customer_register/",views.customer_register,name="customer_register"),
    path("seller_register/", views.seller_register, name="seller_register"),
    path("admin_dash/",views.admin_dash,name="admin_dash"),
    path("customer_dash/",views.customer_dash,name="customer_dash"),
    path("seller_dash/",views.seller_dash,name="seller_dash")



]