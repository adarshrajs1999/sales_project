from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User_model(AbstractUser):
    is_customer=models.BooleanField(default=False)
    is_seller=models.BooleanField(default=False)

class Customer(models.Model):
    user=models.ForeignKey(User_model,on_delete=models.CASCADE,related_name="customers")
    name=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=100)
    email=models.EmailField()
    status1=models.BooleanField(default=0)

    def __str__(self):
        return self.name

class Seller(models.Model):
    user = models.ForeignKey(User_model, on_delete=models.CASCADE, related_name="sellers")
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    status2 = models.BooleanField(default=0)

    def __str__(self):
        return self.name


class mobileproduct(models.Model):
    seller=models.ForeignKey(Seller,on_delete=models.CASCADE,related_name='mobileproducts')
    name=models.CharField(max_length=250)
    brand=models.CharField(max_length=250)
    price=models.CharField(max_length=250)
    description=models.TextField()
    image=models.FileField(upload_to='documents/')
    





