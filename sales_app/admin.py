from django.contrib import admin
from sales_app import models

# Register your models here.
admin.site.register(models.login_view)
admin.site.register(models.Customer)
admin.site.register(models.Seller)