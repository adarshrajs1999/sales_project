from django.contrib import admin
from sales_app import models

# Register your models here.
admin.site.register(models.User_model)
admin.site.register(models.Customer)
admin.site.register(models.Seller)
admin.site.register(models.Product)
admin.site.register(models.Cart)
admin.site.register(models.Buy)
admin.site.register(models.Pay)
admin.site.register(models.Feedback)
