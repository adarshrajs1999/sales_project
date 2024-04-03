from django.urls import path

from sales_app import views

urlpatterns = [
    path("",views.home,name="home"),
    path("dash/",views.dash,name="dash"),
    path("login/",views.login_1,name="login_1")


]