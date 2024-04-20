from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class login_view(AbstractUser):
    is_customer=models.BooleanField(default=False)
    is_seller=models.BooleanField(default=False)

class Customer(models.Model):
    user=models.ForeignKey(login_view,on_delete=models.CASCADE,related_name="customer")
    name=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=100)
    email=models.EmailField()
    status1=models.BooleanField(default=0)

    def __str__(self):
        return self.name

class Seller(models.Model):
    user = models.ForeignKey(login_view, on_delete=models.CASCADE, related_name="seller")
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    status2 = models.BooleanField(default=0)

    def __str__(self):
        return self.name




