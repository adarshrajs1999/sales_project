from django.urls import path

from sales_app import views, admin_views, seller_views, customer_views

urlpatterns = [
    path("", views.home, name = "home"),
    path("dash/", views.dash, name = "dash"),
    path("login/", views.login_view, name = "login_view"),
    path("customer_register/", views.customer_register, name= "customer_register"),
    path("seller_register/", views.seller_register, name = "seller_register"),
    path("admin_dash/",views.admin_dash, name = "admin_dash"),
    path("customer_dash/", views.customer_dash, name = "customer_dash"),
    path("seller_dash/", views.seller_dash, name = "seller_dash"),
    path("customer_details/", admin_views.customer_details, name = "customer_details"),
    path("seller_details/", admin_views.seller_details, name = "seller_details"),
    path("customer_update/<int:id>/", admin_views.customer_update, name = "customer_update"),
    path("seller_update/<int:id>/", admin_views.seller_update, name = "seller_update"),
    path("customer_delete/<int:id>/", admin_views.customer_delete, name = "customer_delete"),
    path("seller_delete/<int:id>/", admin_views.seller_delete, name = "seller_delete"),
    path("add_product/", seller_views.create_product, name = "create_product"),
    path("seller_view_products/", seller_views.seller_view_products, name = "seller_view_products"),
    path("product_delete/<int:id>/", seller_views.product_delete, name = "product_delete"),
    path("update_product/<int:id>/",seller_views.product_update, name = "product_update"),
    path("admin_view_products/", admin_views.admin_view_products, name = "admin_view_products"),
    path("customer_view_products/", customer_views.customer_view_products, name =  "customer_view_products"),
    path("add_to_cart/<int:product_id>/", customer_views.add_to_cart, name = "add_to_cart"),
    path("view_cart/", customer_views.view_cart, name = "view_cart"),
    path("delete_cart/<int:id>/", customer_views.delete_cart, name = "delete_cart"),
    path("buy/<int:cart_id>/", customer_views.buy, name = "buy"),
    path("payment/<int:buy_id>/", customer_views.pay, name = "pay"),
    path("view_view_paid_cart/", seller_views.view_paid_cart, name = "view_paid_cart"),
    path("view_my_orders/", customer_views.view_my_orders, name = "view_my_orders"),
    path("customer_feed_back/", customer_views.customer_feed_back, name="customer_feed_back"),
    path("customer_view_feedbacks/", customer_views.customer_view_feedbacks, name="customer_view_feed_backs"),
    path("admin_view_feedbacks/", admin_views.admin_view_feedbacks, name="admin_view_feed_backs"),
    path("admin_view_orders", admin_views.admin_view_orders, name="admin_view_orders"),
    path("admin_update_reply/<int:feedback_object_id>", admin_views.admin_update_reply, name="admin_update_reply")

]