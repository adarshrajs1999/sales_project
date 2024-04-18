from django.urls import path

from sales_app import views

urlpatterns = [
    path("",views.home,name="home"),
    path("dash/",views.dash,name="dash"),
    path("login/",views.login_1,name="login_1"),
    path("customer_register/",views.customer_register,name="customer_register"),
    path("seller_register/", views.seller_register, name="seller_register")



]