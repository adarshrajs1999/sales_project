from django.urls import path

from sales_app import views, admin_views, seller_views, customer_views

urlpatterns = [
    path("",views.home,name="home"),
    path("dash/",views.dash,name="dash"),
    path("login/",views.login_view,name="login_view"),
    path("customer_register/",views.customer_register,name="customer_register"),
    path("seller_register/", views.seller_register, name="seller_register"),
    path("admin_dash/",views.admin_dash,name="admin_dash"),
    path("customer_dash/",views.customer_dash,name="customer_dash"),
    path("seller_dash/",views.seller_dash,name="seller_dash"),
    path("customer_details/", admin_views.customer_details, name="customer_details"),
    path("seller_details/", admin_views.seller_details, name="seller_details"),
    path("customer_update/<int:id>/", admin_views.customer_update, name="customer_update"),
    path("seller_update/<int:id>/", admin_views.seller_update, name="seller_update"),
    path("customer_delete/<int:id>/", admin_views.customer_delete, name="customer_delete"),
    path("seller_delete/<int:id>/", admin_views.seller_delete, name="seller_delete"),
    path("add_product/",seller_views.create_product,name="create_product"),
    path("seller_view_products/", seller_views.seller_view_products, name="seller_view_products"),
    path("product_delete/<int:id>/",seller_views.product_delete,name="product_delete"),
    path("update_product/<int:id>/",seller_views.product_update,name="product_update"),
    path("admin_view_products/", admin_views.admin_view_products, name="admin_view_products"),
    path("customer_view_products/", customer_views.customer_view_products, name="customer_view_products")



]